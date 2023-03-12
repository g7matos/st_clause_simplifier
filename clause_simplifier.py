import openai
import streamlit as st

openai.api_key = st.secrets["key_openai"]

st.title("Hi LEX!")
st.markdown(
    "This mini-app that simpyfies contractual clauses using OpenAI's GPT-3 based [Davinci model](https://beta.openai.com/docs/models/overview)"
)
st.spinner(text="Simplifying...")


def generate_response(prompt):
    completions = openai.Completion.create (
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.3,
    )

    message = completions.choices[0].text
    return message



def get_input():
	input_text = st.text_area("Paste your clause", label_visibility="hidden", placeholder="Paste your clause", height=300)
	return input_text


user_input = get_input()

st.write(st.secrets["prompt_hilex"] + user_input)

if user_input:
	output = generate_response(st.secrets["prompt_hilex"] + user_input)
	st.write(output)
