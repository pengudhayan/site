from PIL import Image
import requests

import streamlit as st
#from streamlit_lottie import st_lottie

def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json
import streamlit as st

st.title("Family")

import streamlit as st

    # --- LOAD ASSETS ---
#lottie_coding = load_lottieurl("https://assets5.lottiefiles.com/packages/lf20 fcfjwiyb.json")
img_contact_form = Image.open("images/18.jpg")
# --- PROJECTS ---
with st.container():
    image_column, text_column = st.columns ((1, 2))
with image_column:
    st.image(img_contact_form)

with text_column:

    st.subheader("Mother")
    st.write("My mother is a woman like no other. Ligaya S. Malbas. 51 yrs. old. To me, my mother is my everything. She is the one who loves me unconditionally and would do everything for us. She is someone who I can always count on. She is forgiving and understands us when we make mistakes. Whatever I am today is solely due to my mother's presence in my life, as she was present for both my successes and failures.")

import streamlit as st

    # --- LOAD ASSETS ---
#lottie_coding = load_lottieurl("https://assets5.lottiefiles.com/packages/lf20 fcfjwiyb.json")
img_contact_form = Image.open("images/16.jpg")
# --- PROJECTS ---
with st.container():
    image_column, text_column = st.columns ((1, 2))
with image_column:
    st.image(img_contact_form)

with text_column:

    st.subheader("Father")
    st.write("I have not seen any superhero, but I have seen my papa. Dionesio T. Malbas. 50 yrs. old. My father plays an important role in our family. My father is the person that I admire the most in my life. I always feel lucky anytime I remember that he is my father knowing how he has done the very best for me in life. He is the one whom I can rely upon blindly during any hour of need and I know that he shall be there for me.")
    
import streamlit as st

    # --- LOAD ASSETS ---
#lottie_coding = load_lottieurl("https://assets5.lottiefiles.com/packages/lf20 fcfjwiyb.json")
img_contact_form = Image.open("images/15.jpg")
# --- PROJECTS ---
with st.container():
    image_column, text_column = st.columns ((1, 2))
with image_column:
    st.image(img_contact_form)

with text_column:

    st.subheader("Older Brother")
    st.write("The only person who can truly understand me, also my enemy. Dionesio S. Malbas Jr. 27 yrs. old. I cherish my brother greatly because he has taught me many things in life as well as lessons, all of which I have come to realize that I have used. He has been there to support me in my many decisions, whether they were smart of foolish ones. He has always been an inspiration to me because he has great example for me to follow. He is always helping my parents with anything they need and does many errands around the house.")

import streamlit as st

    # --- LOAD ASSETS ---
#lottie_coding = load_lottieurl("https://assets5.lottiefiles.com/packages/lf20 fcfjwiyb.json")
img_contact_form = Image.open("images/21.jpg")
# --- PROJECTS ---
with st.container():
    image_column, text_column = st.columns ((1, 2))
with image_column:
    st.image(img_contact_form)

with text_column:

    st.subheader("Youngest Brother")
    st.write("The most annoying little brother in the world. Daniel S. Malbas. 13 yrs. old. We both love to spend time with each other. It only grows stronger with time. There are occasional fights and arguments. But at the end of the day, he and I are always looking after each other. Sometimes he can be annoying, but their presence matters. No matter how many times we fight, the very next day everything would be fine.")