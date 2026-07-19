import streamlit as st
import requests
import random


st.title('AI Image Creator Studio')
user_input=st.text_input('Describe your masterpiece')

st.sidebar.title('Generate Settings')
art_style=st.sidebar.selectbox("Select art style",
                     ['Photorealistic','3D render','Pixer style','Ghibli','Sketch','Manga','Anime','Cartoon'])

#task:3 Added magic enhancer

magic_enhancer=st.sidebar.checkbox("✨ Enable Magic Enhance")

Width=st.sidebar.slider("Image Width",min_value=256,max_value=1024,value=512,step=16)
Height=st.sidebar.slider("Image Height",min_value=256,max_value=1024,value=512,step=16)


#task4: Adding suprise prompts
surprise_prompts = [
    "An astronaut riding a horse on Mars",
    "A cyberpunk street food vendor in Tokyo",
    "A majestic dragon guarding a glowing neon castle",
    "An ancient library floating among the clouds with magical books",
    "A futuristic city where trees are made of glowing glass shards"
]


#creating columns to place generate and suprise button side by side cleanly
col1,col2=st.columns(2)

with col1:
    generate_button = st.button("GENERATE IMAGE")

with col2:
    surprise_button = st.button("🎲 Surprise Me!")

#created an active prompt
active_prompt= None

#setting active_prompt based on which button clicked
if generate_button:
    if user_input:
        active_prompt=user_input
    else:
        st.error("Please enter a description first!!")

elif surprise_button:
    active_prompt=random.choice(surprise_prompts)
    st.info(f"Surprise prompt selected:{active_prompt}")
    


#make image on the base of which active_prompt exists
if active_prompt:
    with st.spinner("Creating your Image"):
        full_prompt=f"{active_prompt} make the art style: {art_style}"

        if magic_enhancer:
            full_prompt+=", crafted as an '8k resolution' 'highly detailed' 'masterpiece' 'trending on artstation' with an 'unreal engine 5 render look'. "


        url = f"https://image.pollinations.ai/prompt/{full_prompt}"
        query_parameters = {
                "width": Width,
                "height": Height
        }
        response=requests.get(url,params=query_parameters)

        if response.status_code==200:
            #convert binary to image
            st.image(response.content,caption=user_input)
            #task2: dynamic file name
            downloaded_picture_name=f"{art_style.lower( ).replace(' ','_')}.png"
            st.download_button(
                                  label="Download Image",
                                  data=response.content,
                                  file_name=downloaded_picture_name,
                                  mime="image/png"
                                   )
        else:
            st.error("ERROR")