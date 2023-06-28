import streamlit as st
import joblib, os
# import os
import pandas as pd

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
    background-image: url("https://dub01pap001files.storage.live.com/y4mfRIuvGIqA97lfg9lOiNN-ap3Jl5vOscqjyfQh6r0mnARMgQZNOaYxzHZEfEK0bFeKJDhfQ5jCc7GfAJOu4j7MFnpfLxNzarkln42DTLJGz7s6Mtd-Fje0rhZ0RLL2jUMT01dcSKUDoR8MXAvw5-W-0DCfuaQLH5U1e6v5fOfgPCsCAK9U-jZRipqVFEyP6j_HZSFvIyc654QRzlmLo7q3tILya3Y50k84VVv54cMFts?encodeFailures=1&width=799&height=763");
    background-size: 180%;
    background-position: top left;
    background-repeat: no-repeat;
    background-attachment: fixed;
}

[data-testid="stSidebar"] > div:first-child {
    background-color: #d5d7db;
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


# Vectorizer
news_vectorizer = open("resources/tfidfvect.pkl","rb")
tweet_cv = joblib.load(news_vectorizer) # loading your vectorizer from the pkl file

# Define the models and their respective vectorizers
models = {
    "Logistic Regression": {
        "model_file": "resources/Logistic_regression.pkl",
        "vectorizer_file": "resources/tfidfvect.pkl"
    },
    "Decision Tree Classifier": {
        "model_file": "resources/Decision_Tree_Classifier.pkl",
        "vectorizer_file": "resources/tfidfvect.pkl"
    },
    "Random Forest": {
        "model_file": "resources/Random_Forest_Classifier.pkl",
        "vectorizer_file": "resources/tfidfvect.pkl"
    },
    "Multinomial NB": {
        "model_file": "resources/MultinomialNB.pkl",
        "vectorizer_file": "resources/tfidfvect.pkl"
    },
    "Support Vector": {
        "model_file": "resources/Support_Vector.pkl",
        "vectorizer_file": "resources/tfidfvect.pkl"
    },
    # Add more models here...
}

# Load the raw data
raw = pd.read_csv("resources/train.csv")

# Helper function to load the model and vectorizer
def load_model_and_vectorizer(model_file, vectorizer_file):
    model = joblib.load(open(model_file, "rb"))
    vectorizer = joblib.load(open(vectorizer_file, "rb"))
    return model, vectorizer

def main():
    st.title("Tweet Classifier")
    st.subheader("Climate change tweet classification")

    options = ["Prediction", "Information"]
    selection = st.sidebar.selectbox("Choose Option", options)

    if selection == "Information":
        st.info("General Information")
        st.markdown("Some information here")

        st.subheader("Raw Twitter data and label")
        if st.checkbox('Show raw data'):
            st.write(raw[['sentiment', 'message']])

    if selection == "Prediction":
        st.info("Prediction with ML Models")
        tweet_text = st.text_area("Enter Text", "Type Here")

        model_selection = st.selectbox("Select Model", list(models.keys()))
        model_info = models[model_selection]
        model_file = model_info["model_file"]
        vectorizer_file = model_info["vectorizer_file"]

        if st.button("Classify"):
                        vect_text = tweet_cv.transform([tweet_text]).toarray()
                        model_info = models[model_selection]
                        model_file = model_info["model_file"]
                        vectorizer_file = model_info["vectorizer_file"]
                        predictor = load_model_and_vectorizer(model_file, vectorizer_file)[0]
                        prediction = predictor.predict(vect_text)
                        st.success("Text Categorized as: {}".format(prediction))
              
if __name__ == '__main__':
    main()
