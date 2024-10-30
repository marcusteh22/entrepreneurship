import streamlit as st
import pandas as pd 

st.title("🏛️ Road to Entrepreneurship")
st.text("""
        Providing aspiring entrepreneurs with an actionable guide to gaining fundamental 
        skills and knowledge in entrepreneurship. From ideation to launching.
        """)
st.image("app/a.png", caption="Illustrations by André Ducci")

st.write("")
st.write("")
st.write("")

st.header("📈 Interesting Statistics")
st.subheader("Best Cities and Countries for Startups")
data = pd.read_csv("app/startupCities.csv")
st.write(data)


st.write("")
st.write("")
st.write("")

st.subheader("Unicorns")
st.image("app/unicornPic.png")

st.write("")
st.write("")
st.write("")

st.subheader("Innovation Cycles")
st.image("app/Innovation_Cycles.png")

st.write("")
st.write("")
st.write("")

st.subheader("Innovation Index")
st.image("app/Innovation-Index.png")

st.write("")
st.write("")
st.write("")

st.subheader("Technology Adoption")
st.image("app/TechAdoption.png")
