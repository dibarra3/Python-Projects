import streamlit as st
#st.set_page_config(layout="wide")

col1, col2 = st.columns(2)

with col1:
    st.image("images/pfp.png") #width to change dimension

with col2:
    st.title("Diego Ibarra")
    content = """ Currently studying software development at UTD
    """
    #st.write(content)
    st.info(content)

st.write("Below you can find some apps I have built in Python.\n\n" 
         "Feel free to contact me.")