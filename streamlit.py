"""
    modified by @vboykis
    code by TaeHwan Jung(@graykode)
    Original Paper and repository here : https://github.com/openai/gpt-2
    GPT2 Pytorch Model : https://github.com/huggingface/pytorch-pretrained-BERT
"""
import streamlit as st
from PIL import Image
import json
import random


image = Image.open('venti.png')
st.image(image, use_column_width=True)

st.markdown("The startling thing is how often the founders themselves don't know.")
st.markdown("Half the founders I talk to don't know whether they're default alive or default dead.")

with open('generated_phrases.json','r') as generated_json:
    data = json.load(generated_json)
    phrase = (random.choice(list(data.values())))
    st.markdown(phrase)