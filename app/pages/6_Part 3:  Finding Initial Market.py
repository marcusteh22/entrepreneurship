import streamlit as st

st.header("Finding Initial Market")
st.text("""
        You have an idea of who your customers will be, however most people won't try a new,
        untestd product. This section goes through the different customer types in an 
        adoption curve and teaches you how to identify customers that might be willing to 
        test your MVP.
        """)
st.image("market.png", caption="Illustration by Muhammed Sajid")

st.write("")
st.write("")
st.write("")

st.subheader("Finding the Smallest Market Possible")
st.write("""
         When you first launch a product, don't try to go for a huge market first. Doing that
         would mean facing tons of competition, and it means you have yet to define your market 
         clearly. Starting with a small market helps you "go under the radar" of larger competitors,
         move quicker, and helps you stay laser focus on a small customer segment.

          Here's a process you can follow: 

         1. Find the smallest market possible to gain a foothold
         2. Capture a large portion of that market & dominate
         3. Expand into larger markets 
         """)

st.write("")

st.write("""
         Here are some examples of starting with a small initial market, then expanding: 

         1. Facebook started as a social media platform for Harvard students only, now they're the 
         largest social media group in the world (owning Whatsapp, Instagram, Threads etc)
         2. Tesla started by targeting the luxury electric vehicle market, now they target the mass market
         3. Amazon initially only sold books, now they sell almost everything
         4. Paypal was initially only available for ecommerce customers on Ebay, now it is used by 
         all kinds of businesses
         5. Grab started with only an e-hailing service, now it is a multi-functional app.
         """)

st.write("")
st.write("")

st.subheader("Customer Adoption Curve")
st.write("""
         Most people are not early adopters and innovators. They want the product to be first tested
         and proven before they adopt it. The image below illustrates the different customer types in
         the curve. Customers who fall under the 'innovators' and 'early adopters' category would be 
         more likely to test out your MVP.
         """)
st.image("adoption.png")
st.write("""
1. Innovators:
The first to try, they embrace risks and are willing to invest in new ideas. Their enthusiasm drives early awareness and generates initial buzz.

2. Early Adopters:
Visionary and influential, they seek innovation and set trends for others. Their endorsement signals value and spurs broader interest.

3. Early Majority:
Practical and deliberate, they look for proven success before buying in. Their adoption marks the transition from niche to mainstream.

4. Late Majority:
Skeptical and cautious, they adopt only when the product feels like a necessity. Their choice is driven by pressure or widespread acceptance.

5. Laggards:
Traditionalists who avoid change, they join only when alternatives fade. Often the last to adopt, they value familiarity over innovation.
""")

st.write("")
st.write("")

st.subheader("Identifying Customers that Urgently Need Your Solution")
st.write("""
         Find the 'hair-on-fire customers! 🔥🔥🔥🔥

         "Hair-on-fire" customers are those with an urgent, pressing need for a solution—think of them as people whose "hair is on fire," 
         desperate for something to put it out. These customers are ideal for MVP (Minimum Viable Product) launches because they’re highly 
         motivated to find a solution, willing to try imperfect products, and quick to provide actionable feedback. 
         """)

st.write("")
st.write("")
st.text("""
        Resources: 
        [1] https://www.ycombinator.com/library/5z-the-real-product-market-fit
        [2] https://youtu.be/0C1H0_Uv1us?feature=shared
        [3] https://ondigitalmarketing.com/learn/odm/foundations/5-customer-segments-technology-adoption/
        """)

st.write("")
st.write("")
st.write("")

if st.button("Challenges"):
    st.markdown("""
Challenge 1: List out all your potential customers. Then, cut them down to the smallest possible market you can target.         
""")