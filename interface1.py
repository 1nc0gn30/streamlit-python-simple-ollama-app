import streamlit as st
import subprocess

st.title("Ollama Chat Interface")
user_input = st.text_input("You:", "")

if st.button("Send"):
    if user_input:
        with st.spinner('Waiting for Ollama response...'):
            try:
                print(f"Running Ollama with input: {user_input}")
                result = subprocess.run(
                    ['ollama', 'run', 'nealscoder', user_input],
                    capture_output=True,
                    text=True,
                    timeout=600
                )
                
                print(f"Return code: {result.returncode}")
                print(f"Stdout: {result.stdout}")
                print(f"Stderr: {result.stderr}")
                
                if result.returncode == 0:
                    st.text_area("Ollama:", result.stdout)
                else:
                    st.error(f"Error: {result.stderr}")
                    
            except subprocess.TimeoutExpired:
                st.error("The process timed out. Please try again.")
    else:
        st.warning("Please enter a message.")

