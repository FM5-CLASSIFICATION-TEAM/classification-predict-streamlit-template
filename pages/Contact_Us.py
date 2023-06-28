import streamlit as st

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
    background-color: #d5d7db;
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
def main():
    st.title("We love hearing from you")

    col1_width = 3
    col2_width = 5

    col1, col2 = st.columns((col1_width, col2_width))
    st.write("")
    st.write("")
    st.write("")

    with col1:
        # Content for the left column
        st.subheader("Get in Touch")
        name = st.text_input("Name:")
        email = st.text_input("Email:")
        message = st.text_area("Message:", "")
        send_button = st.button("Send")
        st.markdown(
            """
            <style>
            .get-in-touch {
                background-color: #f2f2f2;
                padding: 10px;
                border-radius: 10px;
            }
            </style>
            """,
            unsafe_allow_html=True
        )
        
    with col2:
        # Content for the right column
        st.markdown('<link href="https://fonts.googleapis.com/icon?family=Material+Icons+Outlined" rel="stylesheet">', unsafe_allow_html=True)
        st.write("")
        st.write("")
        st.write("")
        st.write("")
        st.write("")
        st.subheader("Contact Us")
        st.markdown(
            """
            <div style="background-color: #f2f2f2; padding: 10px; border-radius: 5px;">
                <span class="material-icons-outlined"style="font-size: 16px">attach_email</span> Email: Reception@GlobalSearchAnalytics</p>
                <span class="material-icons-outlined"style="font-size: 16px;">settings_phone</span> TEL: +27 11 456 7095</p>
                <span class="material-icons-outlined"style="font-size: 16px;">location_on</span>Location: 138 Culinary St, Johannesburg, South Africa</p>
            </div>
            """,
            unsafe_allow_html=True
        )
main()