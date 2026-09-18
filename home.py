import streamlit as st
from databaseconnection import  DatabaseConnection
import io
from dataset import Dataset

@st.cache_resource
class Home:

    def main(self):

        try:
            with st.spinner("Loading HomePage...."):
                database = DatabaseConnection()
                data = Dataset()
                database.connect_db()
                db = database.conn.cursor()
                db.execute("SELECT file_data FROM media_files WHERE description = 'Century Celebration....'")
                st.title("Welcome To Rohit Sharma FanClub")
                dataset = data.cleaned_data
                st.subheader("👤 Rohit Sharma ")
                url = db.fetchone()[0]
                col1,col2 = st.columns([1,1.2])
                with col1:
                    st.image(io.BytesIO(url),width=2000)
                with col2:
                    st.write("Rohit Gurunath Sharma (born 30 April 1987) is an Indian international cricketer and the former captain of the India national cricket team in all formats of the game. He is a right-handed top-order batter. He represents Mumbai in domestic cricket and Mumbai Indians in the Indian Premier League. Sharma was a member of the teams that won the 2007 T20 World Cup, the 2013 ICC Champions Trophy and was the winning captain of the 2024 T20 World Cup and the 2025 ICC Champions Trophy. Sharma is acknowledged as one of the greatest opening batsmen of India in ODI format.")
                    st.write("Sharma holds several batting records which include most runs in T20 Internationals, most sixes in international cricket,most double centuries in ODI cricket (3), most centuries at Cricket World Cups (7) and joint most hundreds in Twenty20 Internationals (5).He also holds the world record for the highest individual score (264) in a One Day International (ODI) and also holds the record for scoring most hundreds (five) in a single Cricket World Cup, for which he won the ICC Men's ODI Cricketer of the Year award in 2019.")
                st.divider()

                st.subheader("⭐ Rohit Sharma Overview ")
                col1,col2,col3 =st.columns([1.6,1.2,3])
                with col1:
                    st.write("Total Matches : ",len(dataset))
                    st.write("Total Runs : ",int(dataset["runs"].sum()))
                    st.write("Average : ",round(dataset["runs"].mean(),2))
                    st.write("Strike Rate : ",round(dataset["Strike_rate"].mean(),2))
                    st.write("Best :",int(dataset["runs"].max()))
                with col2:
                    st.write("50s :", ((dataset["runs"] >= 50) & (dataset["runs"] < 100)).sum())
                    st.write("100s :", ((dataset["runs"] >= 100) & (dataset["runs"] < 200)).sum())
                    st.write("200s :", ((dataset["runs"] >= 200) & (dataset["runs"] < 300)).sum())
                    st.write("4s :",dataset["Fours"].sum())
                    st.write("6s :", dataset["Sixes"].sum())
                with col3:
                    db.execute(
                        "SELECT file_data FROM media_files WHERE description = 'Owner Of Pull-Shot'")
                    home2 = db.fetchone()[0]
                    st.image(io.BytesIO(home2),width=2000)
                st.divider()
        except Exception as f:
            # db.conn.rollback()
            st.error("Connection Failed,Check you have strong network connection...! ")


