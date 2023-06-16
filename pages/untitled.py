import streamlit as st
custom_style = """
<style>
.bubble {
  position: relative;
  display: inline-block;
  padding: 10px 20px;
  background-color: #FF9900;  /* Bubble color */
  color: #FFFFFF;  /* Text color */
  border-radius: 50%;
  font-weight: bold;
  text-align: center;
  margin-right: 10px;
}

.bubble:after {
  content: '';
  position: absolute;
  top: 50%;
  left: 100%;
  margin-top: -10px;
  border-width: 10px;
  border-style: solid;
  border-color: transparent transparent transparent #FF9900;  /* Bubble color */
}
</style>
"""
st.markdown(custom_style, unsafe_allow_html=True)
st.title("Contact Us")

st.subheader("Email")
st.markdown('<div class="bubble">✉️</div> CompanyName@WorldWide.com', unsafe_allow_html=True)

st.subheader("Phone")
st.markdown('<div class="bubble">📞</div> +27 10 456-7890', unsafe_allow_html=True)

st.subheader("Address")
st.markdown('<div class="bubble">📍</div> 138 Cullinary St, Johannesburg, South Africa', unsafe_allow_html=True)
