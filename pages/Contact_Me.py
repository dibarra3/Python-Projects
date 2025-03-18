import streamlit as st
import send_email as se

st.header("Contact Me")

with st.form(key="email_form"):
    name = st.text_input("Name")
    email = st.text_input("Email")
    raw_Message = st.text_area("Your Message")
    message = f"""\
Subject: New email from {name}\n
From: {email}
{raw_Message}  
"""
    button = st.form_submit_button("Submit")
    if button:
        se.send_email(message)
        st.info("Email sent")
