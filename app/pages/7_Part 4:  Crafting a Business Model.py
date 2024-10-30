import streamlit as st

st.header("Crafting a Business Model")
st.text("""
        Business models in startups provide a structured framework for how the company plans 
        to create, deliver, and capture value. They serve as a flexible roadmap for testing
        assumptions, refining strategy, and guiding growth amid uncertainty.
        """)
st.image("app/c.png", caption="Illustration by Hurca!")

st.write("")
st.write("")
st.write("")

st.subheader("Business Model for Startups")
st.write("""
         A business model for startups is a flexible framework designed to guide how the company creates, delivers, and captures value. It’s less of a rigid roadmap and more of an evolving hypothesis, allowing founders to outline their initial assumptions about product-market fit, customer segments, revenue streams, and key activities. Since startups operate in highly uncertain and volatile environments, this model is a structured approach to navigating unpredictability and testing core assumptions rather than a fixed plan.

Think of a startup business model as a "plan to get to the real plan." Startups inherently face shifting customer needs, evolving markets, and unforeseen challenges, which makes long-term planning unreliable. Instead, the business model provides a baseline for rapid experimentation and adaptation, helping founders learn what works and pivot when necessary. By leveraging customer feedback, market signals, and data, the model evolves in response to real-world conditions, aligning closer with a viable strategy over time.

Ultimately, a business model for startups isn’t about perfect forecasting—it’s a flexible, learning-focused tool. It empowers founders to de-risk their venture, discover a repeatable and scalable path to growth, to eventually establish a sustainable business model.
         
         Crafting a business model for startups should be an iterative process! 
         """)
st.write("")
st.write("")

st.subheader("The Business Model Canvas")
st.write("The Business Model Canvas is constructed out of nine building blocks — nine blocks that equip you to think of thousands of possibilities and alternatives. Then, find the best ones.")
st.image("app/business_model.png")

st.text("Template from: https://review.firstround.com/to-go-lean-master-the-business-model-canvas/")

st.write("")
st.write("")

st.write("""
         The Business Model Canvas provides a structured yet flexible framework for startups to define and refine their approach to creating value. Here's how startups can fill out each segment, with examples to guide the process:

1. **Customer Segments**: Start by identifying target customer groups. These could be based on demographics, behaviors, or needs. For instance, a ride-sharing app might target young urban professionals and tourists as distinct segments with different needs.

2. **Value Propositions**: Define the unique value you offer each customer segment. What problems do you solve, and how is your solution different? For example, a food delivery startup’s value could be "quick, healthy meals delivered within 30 minutes," which appeals to busy professionals.

3. **Channels**: Identify how you’ll reach and deliver your product to customers. Channels could include online platforms, retail stores, or partnerships. A fitness app might use social media, app stores, and email marketing to attract users and deliver content.

4. **Customer Relationships**: Decide on the type of relationships you’ll establish with each segment. These could range from self-service (like an e-commerce website) to dedicated support (like enterprise software). For instance, an e-learning platform might offer 24/7 customer support for premium users.

5. **Revenue Streams**: Determine how you’ll make money from each customer segment. This could include subscription fees, product sales, or advertising. A SaaS tool for businesses might offer a freemium model, charging for advanced features.

6. **Key Resources**: Identify critical assets like people, technology, or intellectual property. A delivery startup would need logistical assets, a mobile app, and delivery personnel as key resources.

7. **Key Activities**: Outline essential activities that allow you to deliver value, such as product development, marketing, and customer support. For an online marketplace, this might include vetting sellers and managing the platform.

8. **Key Partners**: Define strategic partners that complement your business model. A hardware startup might partner with manufacturers and distributors to ensure product availability and quality.

9. **Cost Structure**: List major expenses tied to delivering your value proposition, such as salaries, technology, and marketing costs. For a software startup, significant costs could include developer salaries and cloud infrastructure fees.

        This framework helps startups validate ideas, identify assumptions, and build a clearer path to scalability and growth.
         """)

st.write("")
st.write("")
st.write("")

if st.button("Challenges"):
    st.markdown("""
Challenge 1: Fill in the business model canvas to craft your business plan.
                """)

