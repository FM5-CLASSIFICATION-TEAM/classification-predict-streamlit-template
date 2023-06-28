import streamlit as st
from PIL import Image

st.set_page_config(page_icon="📊")
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

# Specify the file paths of the images
image2_path = r"pages\business mission.jpg"
image1_path = r"pages\Company-Vision.jpg"
image3_path = r"pages\target.jpg"

def main():
    # Define a CSS style with a background color
    st.markdown(
        """
        <style>
        .my-div {{
            background-color: {#273756};
        padding: 10px;
             border-radius: 5px;
       }}
       </style>
       """,
       unsafe_allow_html=True
    )
    # Add a title
    st.title("About Us")
    # Apply the custom background color
    page_bg = """
    <style>
    body {
        background-color: rgba(211, 211, 211, 0.5);
    }
    </style>
    """
    st.markdown(page_bg, unsafe_allow_html=True)

    # Split the page into two columns
    col1, col2 = st.columns(2)

    # Top part: subtitle and text on the left, picture on the right
    with col1:
        st.write("")
        st.write("")
        st.subheader("Vision")
        st.write("We aspire to be the premium solution provider for your analytic hurdles, shaping the future of insights-driven decision making.")
        st.write("")
        st.write("")
        st.write("")
        st.write("")
        st.write("")
        st.write("")
        st.write("")
        st.write("")
        st.write("")
        # Open the image file
        image2 = Image.open(image2_path)
        st.image(image2, use_column_width=True)
        st.write("")
        st.write("")
        st.write("")
        st.write("")
        st.write("")
        st.subheader("Goal")
        st.write("The golden key is to leave a mark by addressing societal challenges. The drive is to that have positive contributions to the society.")
    # Bottom part: subtitle and text on the right, picture on the left
    with col2:
        # Open the image file
        image1 = Image.open(image1_path)
        st.image(image1, use_column_width=True)
        st.write("")
        st.write("")
        st.write("")
        st.write("")
        st.write("")
        st.subheader("Mission")
        st.write("We pursue to drive organizations to make informed evidence-based conclusions with confidence")
        st.write("")
        st.write("")
        st.write("")
        st.write("")
        st.write("")
        st.write("")
        st.write("")
        st.write("")
        # Open the image file
        image3 = Image.open(image3_path)
        st.image(image3, use_column_width=True)
main()