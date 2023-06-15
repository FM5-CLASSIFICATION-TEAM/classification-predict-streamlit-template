import streamlit as st

def previous_projects():
    """Displays a list of previous projects."""

    st.title("Previous Projects")

    projects = [
        {
            "project": "Social Network Analysis",
            "description": "Applied unsupervised techniques to analyze and discover patterns in social networks. For example, we identified communities, influential users, or detect anomalies in the network structure."
        },
        {
            "project": "Spam Detection",
            "description": "Developed a machine learning model to accurately classify spam emails, enhancing email filtering and minimizing unwanted messages in users' inboxes."
        },
        {
            "project": "Fraud Detection",
            "description": "Developed a machine learning model to identify and prevent fraudulent activities in financial transactions, safeguarding users and minimizing financial risks."
        },
    ]

    # Display projects in a grid layout
    for i in range(0, len(projects)):
        st.write(f"#### {projects[i]['project']}")
        st.write(projects[i]["description"])
        st.write("")

if __name__ == "__main__":
    previous_projects()