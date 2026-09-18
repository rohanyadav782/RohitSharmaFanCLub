import streamlit as st
import smtplib
from email.message import EmailMessage


class ContactSupport:
    def support(self):
        st.subheader("🎧 Contact Support")
        st.caption("while sharing your query/complaint, please make sure you should also mention your user-id/email/phone number to contact")
        self.chat_input = st.chat_input("Ask something about Rohit Sharma...")
        msg = EmailMessage()
        msg["Subject"] = "Mail from user"
        msg["From"] = "yadavrohan869@gmail.com"
        msg["To"] = "rohitsharmafanpage782@gmail.com"
        msg.set_content(self.chat_input)

        try:
            with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
                smtp.login(self.sender_email, self.app_password)
                smtp.send_message(msg)
            print("Email sent successfully!")
        except Exception as e:
            print(f"Error sending email: {e}")
