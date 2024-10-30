# Ollama Chat Interface

This is a Streamlit-based chat interface that integrates with the **Ollama CLI** to enable interactions with models like `nealscoder`.

## Features
- Real-time chat interface to communicate with the Ollama model.
- User input field to send messages.
- Response display area showing model output.
- Handles errors gracefully, including timeouts.

## Prerequisites
Make sure the following are installed and set up:
- **Python 3.8+**
- **Ollama CLI** with proper configuration ([Ollama Setup](https://ollama.com/docs/installation))
- **Streamlit** for running the web interface.

## Installation

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/1nc0gn30/streamlit-python-simple-ollama.git
   cd https://github.com/1nc0gn30/streamlit-python-simple-ollama.git

2. Install Dependencies:

pip install -r requirements.txt


3. Verify Ollama CLI Installation: Ensure the Ollama CLI is installed and configured properly. You can test it by running:

ollama list



Usage

1. Run the Streamlit App:

streamlit run app.py


2. Using the Interface:

Enter your message in the input field and click Send.

Wait for the model response to appear in the text area.

If there is any issue with the model or input, an appropriate error message will be shown.



3. Timeout Handling:

If the command takes longer than 10 minutes, a timeout error will be displayed.




Troubleshooting

Ollama CLI Not Found: Ensure the CLI is installed and available in your system's PATH.

Timeouts: Try shorter inputs if the process takes too long.

Dependencies: If you face issues with missing packages, re-run:

pip install -r requirements.txt


File Structure

interface1.py: Main application script for the chat interface.

requirements.txt: List of dependencies.
