import streamlit as st

def display_team_member(name, description, designation, emoji):
    st.write(emoji)
    st.markdown(f"<h1 style='font-size:25px'><b>{name}</b></h1>", unsafe_allow_html=True)
    st.write(f"*{designation}*")
    st.write(description)
    st.write("---")

def main():
    st.title("Our Team")
    st.write("") # creating an empty space

    sentence = "We are a young and multicultural data science team, working diligently to analyze data from around the world, one dataframe at a time!"
    st.write("") # creating an empty space

    st.subheader(sentence)
    st.write("") # creating an empty space
    st.write("") # creating an empty space
    team_members = [
        {"name": "Koketso Maraba", "description": "Koketso is a passionate data scientist who thrives on transforming complex datasets into actionable insights. When she's not uncovering hidden patterns, you can find her exploring the city's best coffee shops. Sarah is a skilled latte artist, and she can create beautiful designs on your morning brew.", "designation": "Data Enthusiast and Coffee Connoisseur", "emoji": "👨‍💼"},
        {"name": "Mpho Manthada", "description": "Mpho is a wizard when it comes to coding algorithms and building predictive models. But his talents don't stop there. He's also an outdoor enthusiast who loves hiking and rock climbing. Mpho has conquered several challenging peaks, and he believes that the same determination he has on the mountains can be applied to solving complex data problems.", "designation": "Coding Maestro and Outdoor Adventurer", "emoji": "👩‍💻"},
        {"name": "Akule Cekwana", "description": "Akule is a data analytics expert with a keen eye for detail. She excels at dissecting data and extracting valuable insights. But outside the office, Akule has a musical side. She's a skilled pianist and enjoys playing classical compositions. If you're lucky, you might catch her performing at a local jazz club on weekends.", "designation": "Analytics Ninja and Music Aficionado", "emoji": "👨‍💻"},
        {"name": "Nare Moloto", "description": "Nare is a machine learning whiz who can build powerful models with ease. Apart from her coding prowess, she has a deep passion for films. She has an encyclopedic knowledge of movies from different eras and loves discussing intricate plotlines and hidden symbolism. Don't hesitate to ask her for a movie recommendation!s.", "designation": "Machine Learning Guru and Film Buff", "emoji": "👩‍🎨"},
        {"name": "Dumisani Ncubeni", "description": "Dumisani has a knack for transforming complex data into visually appealing and informative visualizations. His charts and graphs are works of art. When he's not crafting data stories, Dumisani explores the culinary world. He enjoys trying new recipes and exploring different cuisines.", "designation": "Data Visualization Prodigy and Foodie", "emoji": "👨‍🔧"},
        {"name": "Tshegofatso Seabi", "description": "Tshego is a statistical genius who can make sense of even the messiest datasets. But when he's not crunching numbers, Tshego is a globetrotter. He's visited over 30 countries and is always planning his next adventure. Ask him about his favorite travel destinations, and you'll get a firsthand account of his unforgettable experiences.", "designation": "Statistical Wizard and Travel Enthusiast", "emoji": "👩‍💼"},
        {"name": "Koketso Makofane", "description": "Koketso is a master at harnessing the power of natural language processing algorithms to extract meaningful information from text data. Off the clock, she immerses herself in the world of books. Koketso is an avid reader who devours literature from various genres. Feel free to discuss the latest bestsellers or ask her for a book recommendation tailored to your tastes.", "designation": "Natural Language Processing Expert and Bookworm:", "emoji": "👩‍💼"}
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
                        team_members[index]["emoji"],
                    )

if __name__ == "__main__":
    main()
