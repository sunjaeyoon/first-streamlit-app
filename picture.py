import streamlit as st
import numpy as np
import os

import matplotlib.pyplot as plt
from PIL import Image
import cv2

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
    img_size = img.shape
    end_width = 500
    scale = end_width/img_size[1]
    
    width = int(img_size[1] * scale)
    height = int(img_size[0] * scale)
    dsize = (width, height)
    #resize the image
    return cv2.resize(img, dsize)

data = load_img(DATA_URL)

#SIDE BAR Options
activities = ["Selection","About"]
choice = st.sidebar.selectbox("Select Activity", activities)

#Selection Choice
if choice =="Selection":
    x = st.slider('x', 0, len(data)-1)
    st.write("You selected", x)
    data[x].shape
    st.image(reSize(data[x]))

#About Choice
if choice =="About":
    st.write("You selected About")

