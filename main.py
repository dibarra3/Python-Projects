import pandas
import streamlit as st
#Panda is used to read CVS files


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

df = pandas.read_csv("data.csv", sep=";")

col3, emptyCol, col4 = st.columns([1.5,0.5,1.5])

with col3:
    for index, row in df[:10].iterrows():
        st.header(row["title"])
        st.write(row["description"])
        st.image("images/" + row["image"])
        st.write(f"[Source Code]({row['url']})")

with col4:
    for index, row in df[10:].iterrows():
        st.header(row["title"])
        st.write(row["description"])
        st.image("images/" + row["image"])
        st.write(f"[Source Code]({row['url']})")