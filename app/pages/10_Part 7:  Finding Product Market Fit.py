import streamlit as st

st.header("Finding Product Market Fit")
st.text("""
        The existance of a startup is to find Product Market Fit, then Scale.
        """)
st.image("app/e.png", caption="Illustration by Febin Raj")

st.write("")
st.write("")
st.write("")

st.subheader("What is PMF")
st.write("""
         **Product-Market Fit (PMF)** is a critical milestone for any startup, marking the point where a product effectively meets the needs of its target market. When PMF is achieved, a startup’s product resonates with customers, solving a meaningful problem or fulfilling a significant demand. This alignment is crucial because it signifies that there is a viable, scalable business opportunity, often evidenced by rapid customer adoption, positive feedback, low churn rates, and a growing willingness to pay. 

    PMF is often regarded as the fundamental reason for a startup’s existence.
    Unlike established businesses, startups are in a constant search for a sustainable business model. 
Their primary goal is not just to create a product but to develop something that truly meets market demand. Startups exist to validate that their solution is valuable, and PMF serves as proof of that validation. In essence, it’s the answer to whether a startup’s hypothesis about its product’s value to customers is correct. Finding PMF signals that the company has not only identified a viable target market but also crafted a product that market genuinely wants.

The importance of PMF cannot be overstated. Achieving it can transform a startup’s growth trajectory, as products with PMF often experience exponential growth. PMF minimizes wasted resources by clarifying which product features, user needs, and market strategies are working. With PMF, the startup has the foundation needed to focus on scaling, marketing, and expansion, whereas without it, any additional investment in growth is likely to result in poor returns. 

Startups that fail to reach PMF often struggle to attract and retain customers, leading to a higher risk of failure. In fact, according to many venture capitalists, the lack of PMF is a leading cause of startup closures. Therefore, for founders, the journey to PMF should be a priority, guiding decisions around product development, customer discovery, and iterative improvement. Once PMF is attained, a startup can confidently invest in scaling, knowing that it has a solid, validated base to grow upon.
         """)

st.write("")
st.write("")
st.write("")

st.subheader("How to Find PMF")
st.write("""
Finding Product-Market Fit (PMF) is an iterative process of refining a product to meet market needs through continuous customer feedback and testing. Startups begin by identifying a core problem and launching a Minimum Viable Product (MVP) to address it. By getting the MVP into users' hands quickly, startups can gather real customer data to see how well the product meets the intended need.

Feedback loops are crucial for achieving PMF. Through customer conversations, testing, and observing, startups can learn what resonates with users and where improvements are needed. Each iteration should be about learning what customers truly want. 
Once customers show genuine interest through indicators like organic growth, word-of-mouth referrals, and high engagement, the startup is closer to achieving PMF. This foundation paves the way for sustainable growth, as PMF allows for confident scaling of the business.
         
         The key to finding PMF is through an iterative, experimental process that is methodical.
""")

st.write("")
st.write("")
st.write("")

st.text("""
        Resource: 
        [1] https://a16z.com/12-things-about-product-market-fit/
        [2] https://pmarchive.com/guide_to_startups_part4.html
                """)

st.write("")
st.write("")
st.write("")

if st.button("Challenges"):
    st.markdown("""
Challenge 1: Study a company. What was their first product, and how they iterated or pivoted to eventually find PMF""")
