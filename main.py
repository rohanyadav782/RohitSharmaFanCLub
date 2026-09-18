from prediciton import Prediciton
from dashbd import Dashboard
from Ai import AiAssistant
from home import Home
from fan_page import FanPage
from loginpage import LoginPage
from aboutproject import AboutProject
from profile import Profile
from dataset import Dataset

import streamlit as st

st.set_page_config(
    page_title="Rohit Sharma Fan Club",
    page_icon="🏏",
    layout="centered"
)
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

if "user_id" not in st.session_state:
    st.session_state.user_id = None

class Main:
    def main(self):
        if not st.session_state.logged_in:
            login = LoginPage()
            login.main()

            # Stop main.py here
            return
        st.sidebar.success(
            f"Welcome {st.session_state.user_id} 👋"
        )
        menu = st.sidebar.radio(
            "",
            ["🏠 Home","❤️ FanClub","📰 DataSet","🎯 Prediction","📈 Dashboard"," 🧠 AI Assistant"," 👤 My Profile","🔍 About Project"])

        if menu == "🏠 Home":
            home=Home()
            home.main()

        if menu =="❤️ FanClub":
            fanpage=FanPage()
            fanpage.run()

        if menu == "🎯 Prediction":
            prediction = Prediciton()
            prediction.load_files()
            prediction.predict_runs()

        if menu == " 🧠 AI Assistant":
            ai = AiAssistant()
            ai.main()

        if menu =="📈 Dashboard":
            dashboard = Dashboard()
            dashboard.main()

        if menu == "🔍 About Project":
            info = AboutProject()
            info.main()

        if menu == " 👤 My Profile":
            showprofile = Profile()
            showprofile.main()

        if menu == "📰 DataSet":
            data = Dataset()
            data.main()


        if st.sidebar.button("➜] Logout",use_container_width=True
        ):
            with st.spinner("Logging out...."):
                st.session_state.logged_in = False
                st.session_state.user_id = None
                st.sidebar.warning("Logout Successful!")
                st.cache_data.clear()
                st.cache_resource.clear()

                st.rerun()

app = Main()
app.main()
