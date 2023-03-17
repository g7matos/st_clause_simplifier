import openai
import streamlit as st

openai.api_key = st.secrets["key_openai"]

st.title("Hi LEX!")
st.spinner(text="Simplifying...")


with st.sidebar:
    st.markdown("""
    # About 
    This is a mini-app that uses GPT-3 to rewrite clauses.  
    """)
    st.markdown("""
    Made by [Gustavo Matos](https://www.linkedin.com/in/gfmatos/)
    """)




def generate_response(prompt):
    completions = openai.Completion.create (
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=1624,
        n=1,
        stop=None,
        temperature=0.7,
    )

    message = completions.choices[0].text
    return message



def get_input():
    input_text = st.text_area("Paste your clause", label_visibility="hidden", placeholder="Paste your clause", height=300)
    return input_text

user_input = get_input()

if st.button("Simplify"):
    prompt =" ".join([st.secrets["prompt_hilex2"], user_input])
    st.write(generate_response(prompt))