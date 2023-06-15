import streamlit as st

def display_team_member(name, description, designation, emoji):
    st.write(emoji)
    st.write(f"**{name}**")
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
        {"name": "John Doe", "description": "Lorem ipsum dolor sit amet, consectetur adipiscing elit.", "designation": "CEO", "emoji": "👨‍💼"},
        {"name": "Jane Smith", "description": "Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris.", "designation": "CTO", "emoji": "👩‍💻"},
        {"name": "Alex Johnson", "description": "Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore.", "designation": "Developer", "emoji": "👨‍💻"},
        {"name": "Sarah Davis", "description": "Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt.", "designation": "Designer", "emoji": "👩‍🎨"},
        {"name": "Michael Brown", "description": "Sed ut perspiciatis unde omnis iste natus error sit voluptatem.", "designation": "Manager", "emoji": "👨‍🔧"},
        {"name": "Emily Wilson", "description": "At vero eos et accusamus et iusto odio dignissimos ducimus qui blanditiis.", "designation": "Analyst", "emoji": "👩‍💼"},
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
