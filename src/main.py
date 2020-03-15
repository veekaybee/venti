from PIL import Image
import json
import random
import streamlit as st

st.markdown("## Refresh to create a new thinkpiece.")

image = Image.open('src/venti.png')
st.image(image, use_column_width=True)


with open('fixed_generated_phrases.json', 'r') as generated_json:
    data = json.load(generated_json)
    phrase = random.choice(list(data.values()))
    st.markdown(str(phrase))


st.markdown("Made with 💖 by [Vicki Boykis](http://www.vickiboykis.com)")
st.markdown("More about the project [here](http://www.vickiboykis.com)")