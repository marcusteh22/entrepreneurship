import streamlit as st

st.header("Pricing Your Product")
st.text("""
        Pricing is a science, but it is also an art, one that relies on the understanding 
        of marketing and psychology.
        """)
st.image("d.png", caption="Illustration by Hurca!")

st.write("")
st.write("")
st.write("")

st.subheader("Guide to Pricing")
st.write("""
         1. Pricing without Competitors

Startups often lack direct competitors, making it difficult to use market rates as a guide. When you're offering something unique, like a new software solution or innovative gadget, traditional pricing models may not apply. Instead, you’re left to hypothesize the value your product brings to customers and adjust based on feedback. For instance, early in their journey, companies like Uber and Airbnb had to experiment with pricing structures to find what users found reasonable and appealing, since traditional transportation and hotel industry pricing models didn’t directly apply.

2. No Exact Formula, Just Hypotheses and Judgment
         
There’s no one-size-fits-all formula for setting a price. Startups need to approach pricing as a hypothesis—an idea that should be tested, evaluated, and refined over time. This might involve A/B testing different price points, gathering customer feedback, and observing how pricing affects customer acquisition and retention. Pricing is a combination of data-driven decision-making and intuitive judgment, with adjustments over time as the market responds.

3. Perceived Value Drives Pricing Power
         
The ability to charge higher prices largely depends on perceived value rather than production costs. Companies like Apple and LVMH demonstrate this well: Apple can charge a premium for its iPhones not because the hardware costs more than competitors but because customers perceive them as high-quality, innovative, and stylish. Similarly, luxury brands like Louis Vuitton rely heavily on the perceived exclusivity and status associated with their products, allowing them to command significantly higher prices. Startups can leverage this by focusing on the unique benefits and emotional appeal of their products.

4. Price as Part of Brand Story
         
Your pricing communicates more than the cost of production—it conveys quality, brand story, and market positioning. Pricing too low can make your product seem cheap or untrustworthy, while a higher price can imply quality and exclusivity. Think of it as a branding tool that positions your product in the minds of your target audience. 

5. Pricing Choices: Finding the Balance
         
Offering different price points can expand your customer base, allowing you to reach diverse demographics. For example, Apple offers multiple storage options for iPhones, catering to different budgets while maintaining brand consistency. However, providing too many choices can overwhelm customers, leading to "choice paralysis," where potential buyers are so uncertain about which option to pick that they decide to buy nothing at all. Keep choices streamlined to avoid this effect.

6. Example of how pricing affects our purchase decisions
       
""")
st.write("")
st.image("pricing.png")

st.write("")
st.write("")
st.write("")

st.subheader("Here are some commonly used pricing strategies")
st.image("price.png")

st.write("")
st.write("")
st.write("")

st.subheader("Common Pricing Mistakes")
st.write("""
**Mistake #1: Pricing Without Customer Input** 
          
Too often, founders set prices through internal research or benchmarking rather than engaging directly with customers. To truly understand what customers value and are willing to pay, founders should prioritize frequent customer conversations—ideally 3-5 meetings daily. This direct feedback provides insights that no amount of behind-the-desk analysis can match.

**Mistake #2: Treating Initial Pricing as Permanent**  
         
Founders often fall into the trap of picking an initial price and sticking to it as if it’s a fixed solution, even as the business evolves. It’s essential to remember that the first price should be a flexible starting point. As the business and market change, so too should pricing.

**Mistake #3: Setting Prices Too Low**  
         
Many startups undervalue their products, fearing that higher prices will scare off customers or be hard to increase later. However, starting low can stifle growth and set an expectation of low value. Instead, founders should let the market determine the upper bounds of pricing, avoiding unnecessary discounting.

**Mistake #4: Overly Complex Pricing Structures**  
         
In competitive markets, complex pricing models can be a barrier. Customers prefer familiar structures—like monthly subscriptions or per-transaction fees. Overly complex pricing can confuse prospects and slow adoption. Keep it simple and aligned with industry norms.
         """)

st.write("")
st.write("")
st.text("""
        Resouce: 
        [1] https://articles.sequoiacap.com/pricing-your-product
        [2] https://zapier.com/blog/pricing-strategy/ 
        [3] https://review.firstround.com/pricing-lessons-from-working-with-30-seed-and-series-a-b2b-startups/
        """)

st.write("")
st.write("")
st.write("")

if st.button("Challenges"):
    st.markdown("""
Challenge 1: Study each one of these pricing strategies""")
    st.image("price.png")