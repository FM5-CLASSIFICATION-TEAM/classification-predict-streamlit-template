import streamlit as st
import requests
import base64

st.set_page_config(page_icon="📊")
def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()


def get_img_as_base64(file):
    with open(file, "rb") as f:
        data = f.read()
    return base64.b64encode(data).decode()

def get_img_as_base64(file):
    with open(file, "rb") as f:
        data = f.read()
    return base64.b64encode(data).decode()

image_file = "pages\image.jpg"
img = get_img_as_base64(image_file)

# img = get_img_as_base64("image.jpg")

page_bg_img = """
<style>
[data-testid="stAppViewContainer"] > .main {
    background-image: url("https://dub01pap001files.storage.live.com/y4m0zhe1eD5bjr2EuzJx_RNPZ4el2WXGnUJII92Pcvu0wLJWn3ZAfFSGn5D1QJqfSbrs_wMzv7ERTCh2XEuEN97ODfaO-tG9Rw8RAuDv86rEksU8aSRLUjuXj8LKV-Z3v-YjFxGuuJ5R0j38Ly0PVXgPLXvhpWmJ0PCeiLatRqIhl1r9XwEMvZ7OZPUaGe93SFlrQD_gwFP9Z2tL2oJjk90hQald5EhmJV7IT5ENBsDi0Y?encodeFailures=1&width=799&height=763");
    background-size: 180%;
    background-position: top left;
    background-repeat: no-repeat;
    background-attachment: fixed;
}

[data-testid="stSidebar"] > div:first-child {
    background-color: #1C2433;
}

[data-testid="stSidebar"] a {
    color: white !important;
    /* Additional sidebar styles */
    /* ... */
}

[data-testid="stSidebar"] a:hover {
    background-color: #2E3A4F;
}

[data-testid="stHeader"] {
    background: rgba(0, 0, 0, 0);
}

[data-testid="stToolbar"] {
    right: 2rem;
}
</style>
"""
st.markdown(page_bg_img, unsafe_allow_html=True)
# Define file paths
image_file = r"pages\image.jpg"
logo_image = r"pages\logo.png"
chatimage = r"pages\chat.png"

# Load image as base64
image_base64 = get_img_as_base64(image_file)

# Set page background image
page_bg_img = f"""
<style>
body {{
    background-image: url("https://images.unsplash.com/photo-1521080755838-d2311117f767?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&w=1262&q=80");
    background-size: 180%;
    background-position: top left;
    background-repeat: no-repeat;
    background-attachment: fixed;
    font-family: Helvetica, Arial, sans-serif;  /* Set font to Helvetica */
}}
</style>
"""
st.markdown(page_bg_img, unsafe_allow_html=True)

# Load Lottie animation
lottie_coding = load_lottieurl("https://assets7.lottiefiles.com/packages/lf20_KCYk5H7cJP.json")

# Landing Page
st.image(logo_image, use_column_width=True)

# Welcome message
st.title("Welcome to the Climate Change tweet classification app")
st.markdown("""
Are you curious about how people feel about climate change on Twitter? Our sentiment analysis app can help you gain insights by analyzing the sentiment expressed in tweets.
""")

# How it works section
with st.container():
    st.write("---")
    left_column, right_column = st.columns(2)
    with left_column:
        st.header("How it works")
        st.write("##")
        st.write(
            """
            **Write a climate change opinion**: Share your thoughts on climate change by writing a statement or expressing your views.

**Enter your opinion**: Simply enter your opinion in the provided text box. It can be about any aspect of climate change that you feel strongly about.

**Predict sentiment**: Our app utilizes advanced machine learning algorithms to analyze your opinion and predict its sentiment. It classifies your opinion as positive, negative, or neutral based on the sentiment expressed.

**Discover the sentiment**: The app presents the predicted sentiment of your opinion in an easy-to-understand format. You'll see visual indicators or labels representing the sentiment category your opinion falls into
            """
        )
    with right_column:
        st.write("##")
        st.write("##")
        st.write("##")
        st.image(chatimage,  use_column_width=True)

# Why Use Sentiment Analysis section
st.write("---")
st.header("Why Use Sentiment Analysis?")
st.markdown("""
    - **Business Insights**: Understand customer sentiment towards your brand, products, or services to drive business decisions and improve customer satisfaction.
    - **Brand Monitoring**: Organizations continually monitor brand mentions and chatter on social media, forums, blogs, news articles, and other digital platforms. Sentiment analysis technology enable the public relations staff to be aware of ongoing stories that are relevant to their work. To address complaints or capitalize on good trends, the team can assess the underlying mood.
    - **Market Research**: Businesses can improve their product offers by studying what works and what doesn't with a sentiment analysis system. Marketers can acquire deeper insights into certain product characteristics by analyzing comments on online review sites, survey replies, and social media posts. They communicate their results to product owners, who then innovate accordingly.
    - **Track Campaign Perfomance**: Marketers employ sentiment analysis technologies to ensure that their advertising campaign evokes the desired response. They monitor social media conversations to ensure that the overall tone is positive. If the overall attitude falls short of expectations, marketers will make changes to the campaign based on real-time data analytics. 
    - **Opinion Mining**: Identify emerging trends, public opinion shifts, or sentiment patterns in large volumes of text data.
""")

# Start Analyzing Sentiments section
st.write("---")
st.header("Start Analyzing Sentiments Today!")
st.markdown("""
    Click the button below to launch the Sentiment Analysis Tweet Classifier and start gaining valuable insights from Twitter conversations.
""")

# Get Started Button
if st.button("Get Started"):
    # Add your code here to redirect to the actual sentiment analysis app or perform any other action
    st.experimental_set_query_params(page="Base_App.py")
    st.write("Redirecting to the Sentiment Analysis App...")
