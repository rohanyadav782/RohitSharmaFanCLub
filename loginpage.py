import streamlit as st
import psycopg2
import pandas as pd
from sendmsg import SendMsg
from databaseconnection import DatabaseConnection
import io

from contact_support import ContactSupport
message = SendMsg()

@st.cache_resource
class LoginPage:
    def __init__(self):
        try :
            self.db = DatabaseConnection()
            self.db.main()
            self.cursor = self.db.conn.cursor()
            # try :
            self.cursor.execute("SELECT user_id,contact_number,email,password FROM users_data")
            users = self.cursor.fetchall()
            self.df = pd.DataFrame(users, columns=["user_id", "contact_number", "email", "password"])
            self.users_list = self.df["user_id"].tolist()
            self.contact_list = self.df["contact_number"].tolist()
            self.mail_list = self.df["email"].tolist()
            self.cursor.execute("SELECT file_data FROM media_files WHERE description = 'The GOAT🔥'")
            try:
                st.session_state.loginimage = self.cursor.fetchone()[0]
                st.title("🏏 Rohit Sharma FanClub")
                try:
                    st.image(io.BytesIO(st.session_state.loginimage))
                except psycopg2.OperationalError as e:
                    st.error("Network Error!,Try to delete AppCache/Reload page ")

            except Exception as e:
                st.error("Files not initialize, Plz try to delete AppCache/Reload page ")

        except psycopg2.OperationalError as e:
            st.error("Network Error!,Try to delete AppCache/Reload page ")

    def login(self):
        try:
            username = st.text_input("Enter User-ID").lower().capitalize()
            login_password = st.text_input("Enter your Password",type="password",key="Login_password")

            if st.button("Login", icon=":material/thumb_up:", width='stretch'):
                self.cursor.execute("SELECT user_id,contact_number,email,password FROM users_data")
                users = self.cursor.fetchall()
                self.df = pd.DataFrame(users, columns=["user_id", "contact_number", "email", "password"])
                self.users_list = self.df["user_id"].tolist()
                self.contact_list = self.df["contact_number"].tolist()
                self.mail_list = self.df["email"].tolist()
                with st.spinner("Logging your account..."):
                    users_list = self.df["user_id"].tolist()
                    if username not in users_list:
                        st.warning("User not exists")
                    else:
                        actual_password = self.df.loc[self.df["user_id"] == username, "password"].iloc[0]
                        if actual_password != login_password:
                            st.warning("Incorrect password")
                        else:
                            st.session_state.logged_in = True
                            st.session_state.user_id = username
                            st.success("Login Successful!")
                            # ⭐ Go back to main.py
                            st.rerun()

        except Exception as f:
            # self.db.conn.rollback()
            st.error("Network Error!,Try to delete AppCache/Reload page ")


    def creataccount(self):
        st.caption("Make sure, your all credentials fill properly, you may not able to change your details")
        col1,col2 = st.columns(2)
        account_verified = "no"
        try:
            self.cursor.execute("SELECT user_id,contact_number,email,password FROM users_data")
            users = self.cursor.fetchall()
            self.df = pd.DataFrame(users, columns=["user_id", "contact_number", "email", "password"])
            self.users_list = self.df["user_id"].tolist()
            self.contact_list = self.df["contact_number"].tolist()
            self.mail_list = self.df["email"].tolist()

        except Exception as f:
            # self.db.conn.rollback()
            st.error("Unable to load users data...! ")

        with col1:
            name = st.text_input("Enter your full name").title()
            username = st.text_input("Enter User-ID ").lower().capitalize()
            gender = st.selectbox("Select Gender",['Male','Female','Other'],key="Gender Select")
            number = st.text_input("Enter your contact number")
        with col2:
            mail = st.text_input("Enter your email-ID").lower()
            password = st.text_input("Enter your Password",key="new_account_password",type="password")
            msgchoice = st.selectbox("Receive OTP msg on...? ", ["Email", "Contact_Number"],key="OTP msg choice")

            # confirm_password = st.text_input("Confirm Password",type="password")
            otp = st.text_input("Enter OTP here",key ="otp_input")

        with col1:
            if st.button("Send OTP for Verification"):
                with st.spinner("Sending OTP..."):
                    if username in self.users_list or username == "":
                        st.warning("User-ID already taken try different")
                    elif mail in self.mail_list :
                        st.warning("Mail already used!")
                    elif not number.isdigit() or len(number)!=10:
                        st.warning("Please enter valid 10-digit mobile number!")
                    elif int(number) in self.contact_list or number == "" :
                        st.warning("Number already used!")
                    elif not mail.endswith("@gmail.com") or mail == "":
                        st.warning("Please enter valid gmail address!")
                    # elif password!=confirm_password:
                    #     st.warning("Password not matched!")
                    else:
                        if msgchoice=="Email" :
                            message.forgot_password(mail)
                        else:
                            message.forgot_password(number)

        with col2:
            if st.button("Verify your details"):
                with st.spinner("Verifying and creating your account..."):
                    if username in self.users_list or username == "":
                        st.warning("User-ID already taken try different")
                    elif mail in self.mail_list:
                        st.warning("Mail already used!")
                    elif not number.isdigit() or len(number)!=10 or number == "":
                        st.warning("Please enter valid 10-digit mobile number!")
                    elif int(number) in self.contact_list :
                        st.warning("Number already used!")
                    elif not mail.endswith("@gmail.com")  or mail == "":
                        st.warning("Please enter valid gmail address!")
                    # elif password!=confirm_password:
                    #     st.warning("Password not matched!")
                    elif message.otp == "":
                        st.warning("First click on send otp button")
                    elif message.otp != otp:
                        st.warning("Invalid OTP")
                    elif message.otp == otp:

                        self.cursor.execute("""INSERT INTO users_data
                                                                (user_id,name,contact_number,email,password,gender)
                                                                VALUES(%s,%s,%s,%s,%s,%s)""",
                                            (username,name, number, mail, password,gender))
                        self.db.conn.commit()
                        account_verified = "yes"
                        # except Exception as f:
                        #     self.db.conn.rollback()
                        #     st.error("Database Connection Failed,Check you have strong network connection...! ")

        if account_verified == "yes":
            message.welcomemsg(name)
            st.success("Account Successfully Created !,Let's Login and Enjoy")

    def help(self):
            # st.error("Unable to load users data...! ")

        account_verified = "no"
        choice = st.selectbox("Receive OTP msg on...? ",["Email","Contact_Number"])
        if choice == "Contact_Number":
            self.cursor.execute("SELECT user_id,contact_number,email,password FROM users_data")
            users = self.cursor.fetchall()
            self.df = pd.DataFrame(users, columns=["user_id", "contact_number", "email", "password"])
            self.users_list = self.df["user_id"].tolist()
            self.contact_list = self.df["contact_number"].tolist()
            self.mail_list = self.df["email"].tolist()
            col1 , col2 = st.columns(2)
            with col1: 
                self.number = st.text_input("Enter your mobile number","xxxxxxxxxx")
                if st.button("Send OTP"):

                    with st.spinner("Sending otp..."):
                        if int(self.number) not in self.contact_list:
                            st.warning("Number not found!")
                        elif not self.number.isdigit() or len(self.number) != 10:
                            st.warning("Please enter valid 10-digit mobile number!")
                        else:

                            message.forgot_password(self.number)
            with col2:
                manual_otp = st.text_input("Enter OTP here")
                if st.button("Verify OTP"):
                    if message.otp == manual_otp:
                        account_verified="yes"
                    else:
                        st.warning("Invalid OTP")
        elif choice == "Email":
            col1, col2 = st.columns(2)
            with col1:
                self.mail = st.text_input("Enter your email address", "xxxxxx@gmail.com")
                if st.button("Send OTP"):

                    with st.spinner("Sending mail..."):
                        if self.mail not in self.mail_list:
                            st.warning("Mail not found!")
                        else:

                            message.forgot_password(self.mail)
            with col2:
                manual_otp = st.text_input("Enter OTP here")
                if st.button("Verify OTP"):
                    with st.spinner("Verifying OTP..."):
                        if message.otp == manual_otp:
                            account_verified="yes"
                        else:
                            st.warning("Invalid OTP")

        if account_verified=="yes":
            st.success("Account Successfully Verified!")
            if choice == "Contact_Number":
                identifier = self.number
            elif choice == "Email":
                identifier = self.mail
            with st.spinner("Sending Details to user..."):
                try :
                    self.cursor.execute(f"SELECT name,user_id,contact_number,email,password FROM users_data WHERE {choice}='{identifier}'")
                    rows = self.cursor.fetchall()
                    user_detail = [row for row in rows[0]]
                    message.sharedetail(user_detail)
                except Exception as f:
                    # self.db.conn.rollback()
                    st.error("Unable to share detail!")
                    st.error("Connection Failed,Check you have strong network connection and reload it...! ")

    def choice_button(self):

        tab1, tab2 ,tab3 = st.tabs(['Login', "Create New Account","Forgot Account Detail"])
        with tab1:
            self.login()
        with tab2:
            self.creataccount()
        with tab3:
            self.help()

    def main(self):
        self.choice_button()
