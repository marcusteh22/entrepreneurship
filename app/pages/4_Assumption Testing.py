import streamlit as st

st.header("Assumption Testing")
st.text("""
        All initial ideas are merely assumptions. An assumption that the idea is viable,
        an assumption that there is a market for it, an assumption about a customer segment 
        etc. Hence, we must conduct experiments to tests all those assumptions.
        """)
st.image("app/space.png",caption="Illustration by Stefan Große Halbuer")

st.write("")
st.write("")
st.write("")

st.subheader("Conducting Experiments to Test Assumptions")
st.write("""
         To test a viability of an idea, we can conduct the 'Riskiest Assumption Test', which follows
         a 3-step process:

         1. List the assumptions that must be true for your idea to succeed.
         2. Identify which individual assumption is most important for this success.
         3. Design and conduct a test to prove whether this assumption is true or not.
         """)

st.write("")
st.write("")

st.write("""      
         To illustrate this process. Here's a case study on 'DoorDash', a food delivery company:

         In 2012, DoorDash’s founders discovered the unmet demand for delivery services while interviewing 
         small business owners like a macaroon shop owner in Palo Alto, who had numerous delivery requests 
         but no drivers. Recognizing the potential, they focused on testing the riskiest assumption: would 
         customers trust a third-party website for food deliveries? Instead of initially engaging restaurant
         owners, they launched a simple site, paloaltodelivery.com, listing PDF menus and offering a $6 
         delivery service with no minimum order. They quickly validated their assumption when orders started 
         pouring in, primarily from Stanford students, proving that customers would indeed use a third-party 
         delivery service and affirming the viability of their business model.

         They created a simple website to test their assumptions.
         """)

st.image("app/door.png")

st.write("")
st.write("")

st.write("Example of Assumption Board used in the case of DoorDash")
st.image("app/assume_board.png")

st.write("")
st.write("")

st.write("Example of Assumption Board used at Unilever")
st.image("app/unilever.png")

st.write("")
st.write("")

st.write("Case Study of Amazon's Assumption Test")
st.image("app/amazon.png")

st.write("")
st.write("")

st.text("""
        Resources: 
        [1] https://www.opinionx.co/blog/assumption-testing
        [2] https://review.firstround.com/the-minimum-viable-testing-process-for-evaluating-startup-ideas/?action=subscribe&success=true
        """)

st.write("")
st.write("")
st.write("")

if st.button("Challenges"):
    st.markdown("""
Challenge 1: Think of an idea you want to test. Using the framework and templates above, conduct a "Riskiest Assumption Test" to evaluate the viability of your idea.          
""")
