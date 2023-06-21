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
#image_base64 = get_img_as_base64(image_file)

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

def previous_projects():
    """Displays a list of previous projects."""

    st.title("Previous Projects")
    st.markdown("At our company, we prioritize the use of cutting-edge technologies and innovative approaches to deliver exceptional results. Our team of experienced data scientists and machine learning experts is dedicated to providing tailored solutions to address your specific needs. Whether it's social network analysis, spam detection, fraud detection, or any other data-driven project, we are committed to delivering top-notch solutions that exceed your expectations.")

    projects = [
        {
            "project": "Social Network Analysis",
            "description": "One of our notable achievements includes leveraging unsupervised techniques to analyze and discover patterns in social networks. By applying advanced algorithms, we were able to identify distinct communities within networks, pinpoint influential users, and even detect anomalies in the network structure. This valuable insight helps our clients gain a deeper understanding of their social media presence and facilitates targeted marketing strategies."
        },
        {
            "project": "Spam Detection",
            "description": "In an era where email inboxes are flooded with unwanted messages, we took up the challenge of developing an efficient solution. Our team built a robust machine learning model specifically designed to accurately classify spam emails. By analyzing various features and patterns, our model effectively enhances email filtering systems, ensuring that users only receive legitimate and desired content while minimizing the disruption caused by spam."
        },
        {
            "project": "Fraud Detection",
            "description": "Financial fraud poses a significant threat to individuals and organizations alike. To combat this issue, we developed a powerful machine learning model tailored to identify and prevent fraudulent activities in financial transactions. By analyzing transactional data and employing advanced algorithms, our model is capable of detecting suspicious patterns and behaviors, thus safeguarding users from potential financial risks. Our fraud detection system has proven to be highly effective in mitigating fraudulent activities and protecting the interests of our clients."
        },
    ]

    

    # Display projects in a grid layout
    for i in range(0, len(projects)):
        st.write(f"#### {projects[i]['project']}")
        st.write(projects[i]["description"])
        st.write("")
    
    st.markdown("Contact us today to learn more about how our expertise can benefit your organization and help you **harness the power of data** for strategic decision-making. We look forward to collaborating with you and embarking on a successful partnership.")

if __name__ == "__main__":
    previous_projects()