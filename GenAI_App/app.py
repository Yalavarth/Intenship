from openai import OpenAI
import streamlit as st


#Read API key and setup an OpenAI client
f = open(r"C:\Users\Yalavarthi Saadhika\Desktop\.open_API_key.txt")
key = f.read()
client = OpenAI(api_key=key)

prompt = st.text_input("User Input")

def train(prompt):
    response = client.chat.completions.create(
    model="gpt-3.5-turbo-1106",
     messages=[
        {"role": "system", "content": """You are a helpful AI Assistant.

                                     You always fix the python code and fix the bug with the explaination
                                        """},
                        {"role": "user", "content": prompt}
                      ]
                )
    return response.choices[0].message.content


if st.button("Generate"):      
    st.write(train(prompt))