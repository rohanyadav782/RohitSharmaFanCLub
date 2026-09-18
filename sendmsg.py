import random
import streamlit as st
import os
from dotenv import load_dotenv
load_dotenv()
# for message through number
import requests
from requests.auth import HTTPBasicAuth

# for mail
import smtplib
from email.message import EmailMessage

class SendMsg:
    def __init__(self):
        # on number
        self.device_id = os.getenv("mobile_id")
        self.username = os.getenv("mobile_username")
        self.password = os.getenv("mobile_password")
        self.url = os.getenv("mobile_url")

        # for mail
        self.sender_email = os.getenv("sender_email")
        self.app_password = os.getenv("app_password")

    def send_sms(self,number,message):
        payload = {"textMessage": {"text": message}, #required msg
            "deviceId": self.device_id,
            "phoneNumbers": [number], #receiver number
            "simNumber": 1,
            "ttl": 3600,
            "priority": 100}

        response = requests.post(
            self.url,params={"skipPhoneValidation": True,"deviceActiveWithin": 12},auth=HTTPBasicAuth(self.username,self.password),
            json=payload,timeout=20)
        self.status = response.text

    def send_mail(self,receiver_email,message,title):
        msg = EmailMessage()
        msg["Subject"] = title
        msg["From"] = self.sender_email
        msg["To"] = receiver_email
        msg.set_content(message)

        try:
            with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
                smtp.login(self.sender_email, self.app_password)
                smtp.send_message(msg)
            print("Email sent successfully!")
        except Exception as e:
            print(f"Error sending email: {e}")

    def forgot_password(self,receiver_detail):
        self.otp =  str(random.randint(1000, 9999))
        self.OTP = self.otp
        title = "Account Verification Step"
        self.otp_msg = f"""
Hi !

Welcome to rohitsharmafanclub!
verify your account using OTP {self.OTP} 
Don't Share this code with anyone
"""
        if receiver_detail.endswith("@gmail.com"):
            self.send_mail(receiver_detail,self.otp_msg,title)
            st.success("Otp sent to mail!")

        else:
            self.send_sms(receiver_detail,self.otp_msg)
            st.success("Otp sent to number!")

    def sharedetail(self,detail):
        title = "Account Detail Shared By Application"
        self.otp_msg =f"""
Dear {detail[0]},

Here is your account details
Name     :- {detail[0]}
User-ID  :- {detail[1]}
Number   :- {detail[2]}
Email    :- {detail[3]}
Password :- {detail[4]}

Don't Share this credentials with anyone.

Best Regards,
rohitsharmafanclub782
"""
        self.send_sms(str(detail[2]), self.otp_msg)
        self.send_mail(detail[3],self.otp_msg,title)
        st.success("Account Details Shared")

