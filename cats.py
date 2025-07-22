import streamlit as st
import requests
from PIL import Image
from io import BytesIO

st.title("Cat Picker")

if 'cat_img' not in st.session_state:
    st.session_state.cat_img = None

def load_cat_image():
    response = requests.get("https://cataas.com/cat")
    img = Image.open(BytesIO(response.content))
    img = img.resize((300, 300))
    st.session_state.cat_img = img

if st.button("Show me a cat!") or st.session_state.cat_img is None:
    load_cat_image()

if st.session_state.cat_img:
    st.image(st.session_state.cat_img, caption="Do you like this cat?", use_container_width=False)

    col1, col2 = st.columns(2)
    with col1:
        if st.button("Yes"):
            st.success("You picked YES!")
            load_cat_image()
    with col2:
        if st.button("No"):
            st.info("You picked NO!")
            load_cat_image()

