import openai
import streamlit as st

# Set OpenAI API key from Streamlit secrets
openai.api_key = st.secrets["key_openai"]

# Define Streamlit app title and sidebar content
st.set_page_config(page_title="Clause Craft")
st.sidebar.markdown("# Configs")
output_lang = st.sidebar.radio("Output Language:", ["English", "Spanish", "Portuguese"])
st.sidebar.markdown("# About")
st.sidebar.markdown("Clause Craft is a mini-app that uses GPT-3 to rewrite clauses in plain language.")
st.sidebar.markdown("Made by [Gustavo Matos](https://www.linkedin.com/in/gfmatos/)")

# Define function to generate a response using OpenAI GPT-3 API
def generate_response(prompt):
    completions = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=1624,
        n=1,
        stop=None,
        temperature=0.7,
    )
    message = completions.choices[0].text
    return message

# Define function to get user input from a text area
def get_input():
    input_text = st.text_area("Paste your clause", height=300)
    return input_text

# Define Streamlit app content
def main():
    st.title("Clause Craft")
    user_input = get_input()
    if st.button("Craft!"):
        prompt = f"Rewrite the clause in {output_lang} {st.secrets['prompt_hilex2']} {user_input}"
        response = generate_response(prompt)
        st.write(response)

if __name__ == "__main__":
    main()
