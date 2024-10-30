import streamlit as st

st.title("💡 How to Get Startup Ideas")
st.text("""
        How some ideas were generated and turned into billion dollar companies. 
        And a framework on how to generate ideas yourself.
        """)
st.image("leonardo.png", caption="Illustration by Chevalier Gambette")

st.write("")
st.write("")
st.write("")

st.subheader("Startup Ideas")
st.write("""
The best startup ideas come not from forced brainstorming but from observing real, existing problems—ideally ones the founders have experienced personally. Trying to force ideas often leads to what’s known as "sitcom startups": ideas that sound plausible but lack genuine user demand. For instance, while a social network for pet owners might seem appealing because many people care about their pets, in reality, pet owners typically prioritize local networks, veterinarians, or pet services rather than broad social communities focused solely on pets.

Successful startup ideas share three traits: they address a real need the founders themselves feel, they are feasible to build, and they are underappreciated by others. Microsoft, Apple, and Facebook all began as solutions that their founders personally needed, could create, and that few initially recognized as valuable.

A common pitfall for founders is creating "fake" ideas by misjudging users' needs or focusing on a broad audience with minimal interest. Promising startup ideas often start by serving a small, specific group with an urgent need, rather than a broad audience with mild interest. This “well” model—focusing deeply on a niche—often outperforms a shallow, mass-appeal approach. Facebook, for example, started exclusively at Harvard and then expanded, while Microsoft initially built software for Altair users and scaled as demand grew.

Good ideas often arise when founders are deeply engaged in a rapidly evolving field. Instead of trying to "think up" ideas, they notice gaps or unmet needs. Founders who are active at the leading edge of a field often recognize what’s missing and can develop insights that lead to valuable startups.

For those seeking startup ideas, immersing themselves in fields undergoing change, observing unmet needs, and setting aside limiting assumptions can be key. Living in the future and building what’s missing is a formula that has consistently led to successful innovations.
         """)
st.write("")
st.text("Resource: https://www.paulgraham.com/startupideas.html ")

st.write("")
st.write("")
st.write("")

st.subheader("Framework for Generating Ideas")
st.write("""
1. Identify Problems You Face Regularly
Reflect on Daily Challenges: Look for inefficiencies, frustrations, or repetitive tasks in your routine that could be solved with a product or service.

2. Explore Specific Interests and Skills
Leverage Your Expertise: Focus on fields where you have knowledge or skills, as this increases your ability to see gaps and potential solutions.

3. Observe Unmet Needs in Rapidly Changing Fields
Stay Updated on New Trends: Engage with fast-evolving fields (like tech, AI, healthcare) and look for areas where current solutions don’t yet exist.

4. Solve Problems for Niche/Underserved Audiences First
Think Small, Aim Deep: Focus on creating a solution for a small, passionate audience that has a strong need for it, even if the market seems limited.

5. Test “Toy” Ideas That Are Interesting to You
Don’t Overanalyse Initial Scope: Begin by building things that interest you, even if they seem trivial or “toy-like.” Many major startups began as personal or niche projects.

6. "Live in the Future" and Notice What’s Missing
Think from a Forward-Looking Perspective: Imagine what could be needed in the future based on technological trends, and start building solutions for those gaps now.
         """)


st.write("")
st.write("")
st.write("")

if st.button("Challenges"):
    st.markdown("""
Challenge 1: "Customer Journey Mapping" Exercise

Goal: Identify startup opportunities by analyzing pain points in customer journeys.

Instructions:
1. Choose a common process, like booking a vacation or buying a car.
2. Map out every step in the process from start to finish, highlighting points of frustration or delay.
3. Brainstorm how to simplify, automate, or enhance each step

__________________________________________________________________________________________________________________________________________
                

Challenge 2: "Market Gaps" Observation Exercise
                
Goal: Spot gaps in existing markets for potential new ventures.

Instructions:
1. Pick a popular product or service and write down its strengths and weaknesses.
2. Research competitors and their gaps. Look for unmet needs based on customer reviews, forums, or social media comments.
3. Brainstorm ways to address these gaps with a new offering, feature, or product line.


__________________________________________________________________________________________________________________________________________
                

Challenge 3: The "Problem-Driven" Exercise

Goal: Identify specific problems people face and find startup ideas around solutions.

Instructions:
1. List 10 things that frustrate you or people you know daily.
2. For each problem, write down potential solutions. Think about how technology, services, or new models might address these problems in a unique way.
                """)
