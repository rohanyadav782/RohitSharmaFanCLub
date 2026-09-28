import streamlit as st
import psycopg2
import io
from databaseconnection import  DatabaseConnection
from dotenv import load_dotenv
load_dotenv()
import requests
import feedparser

class FanPage:

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
            try:
                url = "https://news.google.com/rss/search?q=cricket&hl=en-IN&gl=IN&ceid=IN:en"
                response = requests.get(url)
                feed = feedparser.parse(response.content)
                news = []
                for article in feed.entries:
                    print(article.title)
                    news.append(article.title)
                all_news = list(set(news))
                for x in range(5):
                    st.write(f"{x+1}. {all_news[x]}")

            except Exception as e:
                st.warning("No News Available !")



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



