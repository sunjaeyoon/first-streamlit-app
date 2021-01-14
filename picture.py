import streamlit as st
import numpy as np
import os

import matplotlib.pyplot as plt
from PIL import Image
st.title("Picture Selector App")
st.text("Pictures to select")

DATA_URL = "../random/delete/"

@st.cache
def load_img(dir_name):
    images = []
    for root, dirs, files in os.walk(dir_name):
        files.sort()
        for f in files:
            if f.endswith((".jpg", "png")):
                pil_image = Image.open(f"{DATA_URL}{f}").convert('RGB')
                open_cv_image = np.array(pil_image)
                images.append(open_cv_image)
        break
    
    return images

def reSize(img):
    size = img.shape
    #resize the image
    return

data = load_img(DATA_URL)

#SIDE BAR Options
activities = ["Selection","About"]
choice = st.sidebar.selectbox("Select Activity", activities)

#Selection Choice
if choice =="Selection":
    x = st.slider('x', 0, len(data)-1)
    st.write("You selected", x)
    st.image(data[x])
