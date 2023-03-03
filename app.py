import streamlit as st
import base64
import json
import random

@st.experimental_memo
def get_img_as_base64(file):
    with open(file, "rb") as f:
        data = f.read()
    return base64.b64encode(data).decode()

bg_img = get_img_as_base64("images/geralt.jpg")
side_img = get_img_as_base64("images/symbol.jpg")

page_bg_img = f"""
    <style>
    .body {{
        font-size:200px;
    }}
    [data-testid="stHeader"]{{
        background-color: rgba(0,0,0,0);
    }}

    [data-testid="stSidebar"]{{
        background-image: url("data:image/jpg;base64,{side_img}");
        background-position: center;
        background-repeat: no-repeat;
    }}
    [data-testid="stMarkdownContainer"]{{
            font-size:large;
            font:20px;
            font-family:Comic Sans MS;
            color:white;
            margin-top:-80px;
            background-position: center;
            text-align: center;

        }}
    [data-testid="stAppViewContainer"]
    {{
        background-image: url("data:image/jpg;base64,{bg_img}");
        background-position: center;
        background-repeat: no-repeat;
        }}

    .title {{
        font-size:60px;
    }}

    .quote {{
        font-size:30px;
        font-family:Comic Sans MS;
        background-color:black;
        opacity:0.8;
        margin-top:100px;
    }}

    [data-testid="stForm"]{{
        background-color:black;
        opacity:0.8;
    }}
    </style>"""

st.markdown(page_bg_img, unsafe_allow_html=True)
st.markdown("<div class='title'> Witcher 3: Quotes </div>",
            unsafe_allow_html=True)

#st.markdown(page_bg_img, unsafe_allow_html=True)

# st.markdown("<div class='title'> Witcher 3: Quotes </div>",
#             unsafe_allow_html=True)


spell = st.secrets["spell"]
st.write(spell)

def get_random_quote():
    with open("quotes.json" , "r") as f:
        quotes = json.load(f)
    return random.choice(quotes)


get_quote = st.button("get_quote")


if get_quote:

    st.write("GETTING RANDOM QUOTE!")
    data = get_random_quote()
    quote = data["quote"]
    author = data["author"]

    col1 , col2 = st.columns(2)

    with col1:
        st.markdown(quote)

    with col2:
        st.markdown(author)
