import streamlit as st

st.title("🔍 Validating Startup Ideas")
st.text("""
        Never fall in love with your ideas. It's crucial to always validate them before 
        spending time building it out. This saves effort, time, and precious resources.
        Part 2 explores the importance of validating startup ideas, and frameworks on 
        how to validate them.
        """)
st.image("b.png", caption="Illustration by Evgenij Kungur")

st.write("")
st.write("")
st.write("")

st.subheader("Reason to Validate Ideas")
st.write("""
         It is easy to fall in love with our own ideas, get excited over it, and jumping straight into it.
         A common mistake founders make is, having a "solution in search of a problem". They trick themselves
         into thinking their idea/solution solves a real problem in the market, when in actual fact, it does 
         not. They try to find a problem to fit their solution. But the correct way is to first identify a 
         problem to solve, then building a solution for it! 

         One of the top reasons startups fail is due to lack of market need. Hence, it is essential to always
         validate them before commiting time, money, and effort on it. 

         The next few sections will discuss ways on how to validate ideas.
         """) 

st.write("")
st.write("")
st.write("")

if st.button("Challenges"):
    st.markdown("""
Challenge 1: Ask yourself do you have "Founder-Market Fit"?

Instructions: Before working on an idea, ask yourself, do you have certain necessary skillsets to work on it, and bring that
              idea to life. Are you capable on working on that specific idea? Are you able to gain the necessary skills and
              knowledge quickly to work on it? 

                
__________________________________________________________________________________________________________________________________________
                

Challenge 2: Ask yourself, does your idea/solution actual solve an actual problem or market need?
                
Instructions: Think deeply about your idea/solution, does it actually solve a problem? What is the problem you're trying to solve?


__________________________________________________________________________________________________________________________________________
                

Challenge 3: Ask yourself, is it something you are willing to spend many years of your life working on?

Goal: Asking yourself this is essential, as building a successful startup takes years! 

""")
