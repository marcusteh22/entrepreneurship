import streamlit as st

st.header("Raising Funds")
st.text("""
        The goal of raising funds is to allow your business to grow and reach the next 
        milestones of the company's lifecycle.
        """)
st.image("money.png", caption="Illustration by Jeff Aphisit")

st.write("")
st.write("")
st.write("")

st.subheader("Essentials of Fund Raising")
st.write("""
1. The Reason for Raising Funds

Raising funds is essential for startups looking to scale, improve their product, and reach key business milestones. Early on, funds are typically needed for product development, securing a team, marketing, and covering operational costs. As a startup grows, additional funding supports market expansion, new product lines, or scaling efforts. Beyond cash flow, raising capital is often about bringing in strategic partners who can offer industry knowledge, connections, or operational support. Investors, especially experienced VCs, often become valuable advisors, sharing insights and opening doors that wouldn’t be accessible otherwise.

2. When to Raise Funds

Timing a fundraise is critical. Generally, founders should look to raise funds when they’ve achieved specific milestones that prove the business model and demonstrate traction. Early funding rounds (like pre-seed or seed) are often sought when a prototype is ready or initial market validation is achieved. Later rounds, such as Series A or B, usually occur when a startup has achieved consistent revenue, solidified product-market fit, or needs capital for scaling. Founders should also consider the fundraising process itself, which can take several months. Planning ahead ensures funds are available before cash flow issues arise, allowing founders to negotiate confidently rather than out of urgency.

3. How Much to Raise

The amount to raise depends on your immediate needs and growth goals. A general rule of thumb is to raise enough to comfortably reach the next significant milestone, such as achieving product-market fit or hitting revenue targets that appeal to larger investors in the next round. This amount should ideally cover 12-18 months of runway, ensuring sufficient funds for growth while preparing for the next raise. Raising too little can lead to frequent fundraising, distracting from business growth, while raising too much too early can dilute equity unnecessarily. Striking a balance based on realistic projections and lean budgeting is key to maximizing both operational flexibility and founder ownership.

4. Creating a Compelling Pitch to Attract Investors:

- Clear Problem and Solution: Define the problem your startup addresses and why your solution is unique. For example, Uber positioned itself as a remedy to unreliable taxi services.

- Market Opportunity: Show the potential size of the market. Investors prefer industries with substantial or growing markets, which suggest room for high returns.

- Business Model and Revenue Streams: Explain how your startup generates revenue. 
         
- Traction and Milestones: Highlight growth metrics, such as user numbers or partnerships. Even early-stage startups can showcase traction through metrics like a growing email list or customer testimonials.
         
5. Considering Alternative Funding Sources

- Venture Capitalists: The most common avenue to raise funds for high-growth startups, they provide capital in exchange for a portion of your company (equity/stake in the company)
         
- Grants: Government grants offer non-dilutive funding (no equity required). 

- Crowdfunding: Platforms like Kickstarter let startups raise funds from the public, often in exchange for early product access. 

- Angel Investors: Angels are usually high-networth individuals that are interested in investing smaller sums of capital (somewhere between 20k to 100K) in early stage startups.
         """)

st.write("")
st.write("")
st.write("")

st.subheader("Example Pitch Decks")
st.write("Uber Pitch Deck")
st.image("uber.png")
st.text("To view full pitch deck: https://www.pitchdeckhunt.com/pitch-decks/uber")

st.write("")
st.write("")
st.write("")

st.write("Canva Pitch Deck")
st.image("canva.png")
st.text("To view full pitch deck: https://www.smartcompany.com.au/startupsmart/advice/canva-first-pitch-deck/")

st.write("")
st.write("")
st.write("")

st.write("Facebook Pitch Deck")
st.image("fb.png")
st.text("To view full pitch deck: https://www.failory.com/pitch-deck/facebook")

st.write("")
st.write("")
st.write("")

st.text("""
        Resource: 
        [1] https://www.ycombinator.com/library/4A-a-guide-to-seed-fundraising#investors-angels-amp-venture-capitalists
        [2] https://about.crunchbase.com/wp-content/uploads/2019/10/Ultimate-guide-raising-startup-capital.pdf
        """)

st.write("")
st.write("")
st.write("")

if st.button("Challenges"):
    st.markdown("""
Challenge 1: Study 3 more companies' pitch decks


______________________________________________________________________________________________________________


Challenge 2: Learn about the different funding rounds:

- pre-seed round
- seed round 
- series A, B, C etc.                         
                """)
    