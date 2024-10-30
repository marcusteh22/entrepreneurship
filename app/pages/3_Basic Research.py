import streamlit as st

st.header("Basic Research")
st.text("""
        When you first conceive an idea, spend some time doing research on Google. Whether
        you're an entrepreneur or a programmer or any other profession, knowing how & what 
        to Google, is an essential skill to have. This section provides you with some 
        advice on what info to search for, while doing research on your idea.
        """)
st.image("app/google.png", caption="Illustration by Ivan Haidutski")

st.write("")
st.write("")
st.write("")

st.subheader("Things to Research")
st.write("1. Has the idea been worked on before?")
st.write("""
         If the idea has already been worked on, ask yourself if it's still something worth pursuing.
         The market might already be crowded. However, it could be that the idea that has been excuted 
         really poorly in the market, hence, might be worth trying to work on.""")

st.write("")
st.write("")

st.write("2. Understanding the market for your idea. Who are your competitors?")
st.write("""
        Using the competitor analysis template below will help you see clearly who your competitors are and 
        how they might defer from you. And how your idea or product is differentiated. 
         """)

st.image("app/comp.png")

st.write("")
st.write("")

st.write("3. What is your Unique Selling Point?")
st.write("""
        After understanding your competitors and their product offerings, how is your product differentiated
        from theirs? And what is your Unique Selling Point?
         """)

st.image("app/usp.png")

st.write("")
st.write("")
st.write("")

st.write("4. Research more about the problem you're trying to solve")
st.write("""
        For example, if you're trying to solve a problem in the education industry, you should do research on
        that particular industry. Understand all its stakeholders, its history, its incentives system etc.
        Having a clear understanding of the problem, will provide you with clarity on what solutions would be
        best used to potentially solve it.
         
        Here's a great quote to illustrate this:
         """)
st.image("app/problem.png")
st.write("")
st.text("Resource: https://www.ycombinator.com/blog/the-real-product-market-fit/")

st.write("")
st.write("")
st.write("")

if st.button("Challenges"):
    st.markdown("""
Challenge 1: Create a competitor analysis, comparing your idea/product with competitors'

                
__________________________________________________________________________________________________________________________________________
                

Challenge 2: List out your idea/product's Unique Selling Point
                

__________________________________________________________________________________________________________________________________________
                

Challenge 3: Select a problem you're interested to know more about, research it, and list out potential
             solutions for it (eg: issues in education, healthcare etc.)

               
""")
