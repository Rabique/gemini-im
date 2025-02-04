import streamlit as st
from PIL import Image
import google.generativeai as genai


st.title("image 파일 업로드")
st.subheader("1. 컴퓨터에 있는 이미지 파일을 업로드")

uploaded_file = st.file_uploader("Image file 선택 " , type = None)

with st.spinner('잠시만 기다려주세요...'):
    
    if uploaded_file:
        image = Image.open(uploaded_file)
        
        
        st.image(image, width=350, caption='컴퓨터에 있는 이미지 파일 표시')
        
        genai.configure()
        model = genai.GenerativeModel("gemini-2.0-flash-exp")
        
        response = model.generate_content(["Tell me about this photo in korean", image])
        st.write(response.text)
st.success('Done!')
