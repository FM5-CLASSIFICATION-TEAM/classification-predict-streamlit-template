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

def display_team_member(name, description, designation, image_path):
    st.image(image_path, caption=name, width=200)
    st.markdown(f"<h1 style='font-size:25px'><b>{name}</b></h1>", unsafe_allow_html=True)
    st.write(f"*{designation}*")
    st.write(description)
    st.write("---")

def main():
    st.title("Our Team")
    st.write("")  # creating an empty space

    sentence = "We are a young and multicultural data science team, working diligently to analyze data from around the world, one dataframe at a time!"
    st.write("")  # creating an empty space

    st.subheader(sentence)
    st.write("")  # creating an empty space
    st.write("")  # creating an empty space
    team_members = [
        {"name": "Koketso Maraba", "description": "Koketso is a passionate data scientist who thrives on transforming complex datasets into actionable insights. When she's not uncovering hidden patterns, you can find her exploring the city's best coffee shops. Sarah is a skilled latte artist, and she can create beautiful designs on your morning brew.", "designation": "Data Enthusiast and Coffee Connoisseur"},
        {"name": "Mpho Manthada", "description": "Mpho is a wizard when it comes to coding algorithms and building predictive models. But his talents don't stop there. He's also an outdoor enthusiast who loves hiking and rock climbing. Mpho has conquered several challenging peaks, and he believes that the same determination he has on the mountains can be applied to solving complex data problems.", "designation": "Coding Maestro and Outdoor Adventurer"},
        {"name": "Akule Cekwana", "description": "Akule is a data analytics expert with a keen eye for detail. She excels at dissecting data and extracting valuable insights. But outside the office, Akule has a musical side. She's a skilled pianist and enjoys playing classical compositions. If you're lucky, you might catch her performing at a local jazz club on weekends.", "designation": "Analytics Ninja and Music Aficionado"},
        {"name": "Nare Moloto", "description": "Nare is a machine learning whiz who can build powerful models with ease. Apart from her coding prowess, she has a deep passion for films. She has an encyclopedic knowledge of movies from different eras and loves discussing intricate plotlines and hidden symbolism. Don't hesitate to ask her for a movie recommendation!s.", "designation": "Machine Learning Guru and Film Buff"},
        {"name": "Dumisani Ncubeni", "description": "Dumisani has a knack for transforming complex data into visually appealing and informative visualizations. His charts and graphs are works of art. When he's not crafting data stories, Dumisani explores the culinary world. He enjoys trying new recipes and exploring different cuisines.", "designation": "Data Visualization Prodigy and Foodie"},
        {"name": "Tshegofatso Seabi", "description": "Tshego is a statistical genius who can make sense of even the messiest datasets. But when he's not crunching numbers, Tshego is a globetrotter. He's visited over 30 countries and is always planning his next adventure. Ask him about his favorite travel destinations, and you'll get a firsthand account of his unforgettable experiences.", "designation": "Statistical Wizard and Travel Enthusiast"},
        {"name": "Koketso Makofane", "description": "Koketso is a master at harnessing the power of natural language processing algorithms to extract meaningful information from text data. Off the clock, she immerses herself in the world of books. Koketso is an avid reader who devours literature from various genres. Feel free to discuss the latest bestsellers or ask her for a book recommendation tailored to your tastes.", "designation": "Natural Language Processing Expert and Bookworm:"},
    ]

    num_members = len(team_members)
    rows = num_members // 3 + (num_members % 3 > 0)

    for i in range(rows):
        cols = st.columns(3)
        for j in range(3):
            index = i * 3 + j
            if index < num_members:
                with cols[j]:
                    display_team_member(
                        team_members[index]["name"],
                        team_members[index]["description"],
                        team_members[index]["designation"],
                        f"team_images/{team_members[index]['name'].replace(' ', '_').lower()}.jpg"
                    )

if __name__ == "__main__":
    main()
