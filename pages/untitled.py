import streamlit as st

st.set_page_config(page_icon="📊")
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