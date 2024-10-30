import streamlit as st

st.header("Minimum Viable Product")
st.text("""
        A minimum viable product is a version of a product with just enough features to
        be usable by early customers who can then provide feedback for future product 
        development. It is also use to test fundamental assumptions about the product
        and ideas.
        """)
st.image("mvp.png", caption="Illustration by Estudio Santa Rita")

st.write("")
st.write("")
st.write("")

st.subheader("The Concept of MVP")
st.write("""
         The concept from the previous chapter, the 'Riskiest Assumption Test' are related concepts,
         and should be used simultaneously with the concept of "MVPs" (Minimum Viable Product). This 
         chapter however, focuses more on the planning and building of something more tangible (a product),
         that is simple, to test ideas and assumptions rapidly and iteratively.
         """)
st.write("""
        A Minimum Viable Product (MVP) is an initial version of a product designed with the minimum features necessary to fulfill its core function, allowing a company to test the concept in the market and gather valuable customer feedback with minimal resources. The MVP approach centers around learning by doing; rather than investing extensive time and money into a fully developed product, companies release a simplified version to assess whether customers find it valuable. This process helps validate core assumptions about user needs, product-market fit, and demand before committing to more substantial development.

Building an MVP involves identifying the product’s essential features—the ones necessary for it to function at a basic level and meet the most critical needs of early adopters. These features should directly align with the problem the product aims to solve, allowing users to understand and experience its main value proposition. By focusing only on the essentials, companies can launch faster, reduce costs, and learn directly from real users. 

The insights gathered from MVP testing help inform product improvements, feature prioritization, and even potential pivots if the initial assumptions prove inaccurate. MVPs can be anything from a simple website to a basic app or prototype, depending on the product. This approach also reduces the risk of investing in a product with little demand, as companies learn early on if users are willing to engage with and pay for it.
""")

st.write("")
st.write("")
st.write("")

st.subheader("Case Study Examples of MVPs")
st.write("""
1. DropBox (Cloud Computing)

Dropbox used an MVP approach by creating a simple video to demonstrate their concept of cloud-based file storage and syncing, rather than building a fully functional product. This video showed how Dropbox would work, allowing users to visualize its benefits without needing a tangible product. By sharing the video, Dropbox's founders gauged user interest and gathered feedback from early adopters. This approach allowed them to validate their 
riskiest assumption—that people would trust and find value in a seamless file-syncing service—without investing heavily in software development. The strong, positive response confirmed demand, allowing Dropbox to proceed with development with confidence that users wanted their solution. This low-cost, feedback-driven MVP strategy ultimately helped Dropbox secure early users and investor interest, setting a solid foundation for the product’s growth.
         
""")
st.write("The video was their MVP")
st.image("dropbox.png")
st.text("Link: https://www.youtube.com/watch?v=w4eTR7tci6A")

st.write("")
st.write("")
st.write("")

st.write("""
2. Zappos (Shoe Ecommerce)
         
Zappos used an MVP approach by testing online demand for shoes without holding any inventory. Founder Nick Swinmurn posted photos of shoes from local stores on a simple website and only purchased the shoes from stores when customers placed orders. This method allowed him to validate the key assumption—that people would buy shoes online—without the financial risk of a large inventory investment. By focusing on learning about customer preferences and online shopping behavior, Zappos gathered essential feedback and refined their processes based on real orders. This MVP approach helped confirm the viability of online shoe sales, leading to Zappos’ rapid growth and eventual acquisition by Amazon.
""")
st.image("zappos.png")

st.write("")
st.write("")
st.write("")

st.write("""
3. Airbnb
""")
st.write("""
Airbnb used an MVP approach by testing demand for short-term home rentals with a simple website. Founders Brian Chesky and Joe Gebbia initially rented out their own apartment in San Francisco to conference attendees who struggled to find hotel rooms. They created a basic site to list their apartment and included pictures of the space, targeting people who needed temporary accommodation. This small-scale test allowed them to validate their riskiest assumption: that people would be willing to rent space in someone’s home instead of a hotel. The positive response confirmed demand, enabling Airbnb to refine its platform and expand to other hosts. This MVP strategy provided essential early insights into user preferences, laying the groundwork for Airbnb’s global success in the short-term rental market.
         """)

st.image("abnb.png")

st.write("")
st.write("")
st.text("Resource/Book: The Lean Startup by Eric Ries")

st.write("")
st.write("")
st.write("")

if st.button("Challenges"):
    st.markdown("""
Challenge 1: Study the MVP of 3 more companies.


__________________________________________________________________________________________________________________________________________
                
Challenge 2: Build an MVP for your idea, and launch it.          
""")
