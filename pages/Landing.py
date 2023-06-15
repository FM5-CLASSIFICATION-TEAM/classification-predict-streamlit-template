import streamlit as st
from streamlit_lottie import st_lottie
import requests
import streamlit as st
from streamlit_lottie import st_lottie

def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()


# ---- LOAD ASSETS ----
lottie_coding = load_lottieurl("https://assets7.lottiefiles.com/packages/lf20_KCYk5H7cJP.json")

st.set_page_config(page_title="Sentiment Analysis Tweet Classifier")

# Landing Page
st.title("Sentiment Analysis Tweet Classifier")

st.markdown("""
            ## Welcome to the Climate change tweet classification!

            Are you curious about how people feel about a specific topic on Twitter? Our sentiment analysis tweet classifier can help you gain insights by analyzing the sentiment expressed in tweets.

""")

with st.container():
    st.write("---")
    left_column, right_column = st.columns(2)
    with left_column:
        st.header("How it works")
        st.write("##")
        st.write(
            """
            1. Enter a keyword or topic of interest in the search box.
            2. Click on the "Analyze" button to start the sentiment analysis process.
            3. Our advanced machine learning algorithm will analyze a stream of real-time tweets related to your keyword or topic.
            4. The classifier will classify each tweet as positive, negative, or neutral based on the sentiment expressed.
            5. The results will be displayed in an easy-to-understand format, allowing you to gauge the overall sentiment surrounding the topic.
            """
        )

    with right_column:
        st_lottie(lottie_coding, height=500, key="coding")

st.write("---")
st.header("Why Use Sentiment Analysis?")
st.markdown("""

            - **Business Insights**: Understand customer sentiment towards your brand, products, or services to drive business decisions and improve customer satisfaction.
            - **Social Media Monitoring**: Monitor public opinion and sentiment about your organization, campaigns, or events on social media platforms.
            - **Market Research**: Gather valuable insights about consumer sentiment towards specific products, competitors, or industry trends.
            - **Brand Reputation Management**: Stay informed about how your brand is perceived by monitoring sentiment in real-time.
            - **Opinion Mining**: Identify emerging trends, public opinion shifts, or sentiment patterns in large volumes of text data.
            """)
st.write("---")
st.header("Start Analyzing Sentiments Today!")
st.markdown("""

            Click the button below to launch the Sentiment Analysis Tweet Classifier and start gaining valuable insights from Twitter conversations.

            
            """)

# Get Started Button
if st.button("Get Started"):
    # Add your code here to redirect to the actual sentiment analysis app or perform any other action
    st.experimental_set_query_params(page="base_app.py")
    st.write("Redirecting to the Sentiment Analysis App...")

