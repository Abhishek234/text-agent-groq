import streamlit as st
import openai
import os
from dotenv import load_dotenv

# Load env variables
load_dotenv()
openai.api_base = "https://api.groq.com/openai/v1"
openai.api_key = os.getenv("GROQ_API_KEY")

# Available tasks
task_options = {
    "Summarize": "Summarize the following in 2–3 sentences.",
    "Rewrite": "Rewrite the text to improve clarity and professionalism.",
    "Compose Email": "Write a polite, professional email based on the following prompt.",
    "Change Tone": "Change the tone of the text to be more friendly and casual."
}

st.set_page_config(page_title="Text Agent", layout="centered")
st.title("🧠 Text Agent")
st.markdown("Choose a task, paste your text, and get instant help.")

# Form UI
with st.form("agent_form"):
    task = st.selectbox("Choose a task", list(task_options.keys()))
    user_input = st.text_area("Enter your text or instruction")
    submitted = st.form_submit_button("Generate")

if submitted:
    if not user_input.strip():
        st.warning("Please enter some text first.")
    else:
        with st.spinner("Thinking..."):
            try:
                response = openai.ChatCompletion.create(
                    model="llama3-8b-8192",
                    messages=[
                        {"role": "system", "content": task_options[task]},
                        {"role": "user", "content": user_input}
                    ],
                    temperature=0.3
                )
                result = response['choices'][0]['message']['content']
                st.success("✅ Done!")
                st.markdown("### ✍️ Result:")
                st.text_area("Output", value=result, height=200)
            except Exception as e:
                st.error(f"❌ Error: {e}")
