import streamlit as st
import psycopg2
import io
from google import genai
from groq import Groq
from databaseconnection import  DatabaseConnection
from dotenv import load_dotenv
load_dotenv()


class FanPage:
    def __init__(self):
        self.model = None
        self.client = genai.Client(
            api_key=st.secrets["GEMINI_API_KEY"])
        self.groq_client = Groq(api_key=st.secrets["GROQ_API_KEY"])

        # System prompt that defines the AI assistant's behavior
        self.system_prompt = """

                        You are an intelligent cricket assistant focused on
                        Rohit Sharma and cricket news.

                        You can share news about :
                        - Rohit Sharma
                        - Any Cricket Player
                        - Any Cricket records
                        - Any Cricket terminology
                        - General cricket information
                        - Anything about Rohit Sharma
                        - Anything about cricket news

                        Give clear, accurate and easy-to-understand answers.

                        Do not claim that information comes from the user's
                        project dataset because the dataset has not been connected yet.

                        Make sure news is related to cricket and rohit sharma else other news is not required and 
                        one more thing new should be genuine not any rumors or fake news should be displayed strictly collect original news no fake news should be showned,
                        Make sure you will answer in only 5 line that is 5 news belongs to cricket and rohit sharma
                        answer like this :1.--------
                                          2.--------
                                          3.--------
                                          4.--------
                                          5.--------
                        any other format is not acceptable
                        Make sure 2 new is belongs to rohit,1 belongs to Indian Player and remaining 2 belongs other cricket information

                """
        try:
            groq_response = self.groq_client.chat.completions.create(
                model="openai/gpt-oss-20b",
                messages=[{"role": "system", "content": self.system_prompt},
                          {"role": "user", "content": "give me exactly 5 cricket news items"}],
                temperature=0.3,
                max_tokens=1000)

            self.news_groq = (groq_response.choices[0].message.content)
            self.model="groq"

        except Exception as e:
            self.response = self.client.models.generate_content(model="gemini-3.6-flash", contents=self.system_prompt + "refresh news dont share recent news")
            st.session_state.response = self.response
            self.model="gemini"


    def show_page(self):
        try :
            self.cursor.execute("SELECT file_data FROM media_files WHERE description = 'profile picture'")
            col1,col2=st.columns([1,2])
            with col1:
                profile_pictore = self.cursor.fetchone()[0]
                st.image(io.BytesIO(profile_pictore))
            with col2:
                self.cursor.execute("SELECT name FROM users_data ")
                fanclub_members =self.cursor.fetchall()
                st.subheader("👥 Rohit Sharma FanClub")
                st.write("Indian Cricket Player")
                st.write(f"👥 Total Members : {len(fanclub_members)}")
                self.cursor.execute("SELECT file_name FROM media_files")
                fanclub_posts =self.cursor.fetchall()
                st.write(f"📝 Total Post : {len(fanclub_posts)}")
        except Exception as f:
            self.db.conn.rollback()
            st.error("Connection Failed,Check you have strong network connection...! ")

    def show_image(self):
        with st.spinner("Loading images..."):
            try :
                self.cursor.execute("SELECT file_data,description FROM media_files WHERE media_type = 'Image' ORDER BY id DESC")
                image_rows = self.cursor.fetchall()
                for image, des in image_rows:
                        st.image(bytes(image))
                        st.write(des)
                        st.divider()
            except Exception as f:
                self.db.conn.rollback()
                st.error("Connection Failed,Check you have strong network connection...! ")


    def news(self):
        with st.spinner("Loading news..."):

            st.subheader("Cricket News")

            if self.model=="groq":
                    st.markdown(self.news_groq)
            else:
                    st.markdown(self.response.text)




    def upload_memory(self):
        file = st.file_uploader("Upload rohit memory")
        if file:
            try :
                with st.spinner("loading image..."):
                    file_bytes = file.getvalue()
                    st.write("Image Preview...")
                    st.image(file)
                    media_type="Image"
                    desc = st.text_input("Enter image Title/Description")
                    if st.button("Upload File"):
                        with st.spinner("Uploading image..."):
                            self.cursor.execute("""INSERT INTO media_files
                                                (file_name,media_type,file_data,description)
                                                VALUES(%s,%s,%s,%s)""",(file.name,media_type,psycopg2.Binary(file_bytes),desc))
                            self.db.conn.commit()
                            st.success("File Uploaded Successfull!")
            except Exception as e:
                st.error(f"Error loading Images : {e}")

    def run(self):
        # self.profile()
        try:
            self.db = DatabaseConnection()
            self.db.connect_db()
            self.cursor = self.db.conn.cursor()
            self.show_page()
            tab1, tab2, tab3 = st.tabs(['🖼️ Rohit Images', "📰 Cricket News","❤️ Upload Rohit Memory"])
            with tab1:
                self.show_image()
            with tab2:
                self.news()
            with tab3:
                self.upload_memory()
        except ValueError:
            st.warning("DB server issue")



