# ZapGPT - AI Chatbot with Llama 3.1

ZapGPT is an AI chatbot application that utilizes the Meta Llama 3.1 405b language model to engage in natural conversations. This project is built using Python and the Streamlit framework for creating interactive web applications.

## Features

- Conversational interface powered by the Llama 3.1 language model
- Ability to maintain chat history and context
- Customizable settings for temperature, top-p, and maximum length of generated responses
- Clear chat history functionality

## Prerequisites

- Python 3.7 or higher
- Streamlit library
- Replicate API token

## Installation

Clone the repository:
bash
git clone https://github.com/caio-videmelo/chatbot-llama3.1_405b

Navigate to the project directory:
bash
cd streamlit_app.py

Install the required dependencies:
bash
pip install -r requirements.txt

Obtain a Replicate API token from https://replicate.com/ and add it to your Streamlit secrets or environment variables.

## Usage

Start the Streamlit application:
bash
streamlit run streamlit_app.py

In your web browser, navigate to the provided URL (usually http://localhost:8501).

Enter your Replicate API token in the sidebar.

Adjust the settings for temperature, top-p, and maximum length as desired.

Type your message in the chat input field and press Enter to generate a response.

The generated response will be displayed in the chat window.

To clear the chat history, click the "Clear Chat History" button in the sidebar.

## Contributing

If you would like to contribute to this project, please follow these steps:

Fork the repository

Create a new branch for your feature or bug fix

Make your changes and commit them

Push your changes to your forked repository

Submit a pull request to the original repository

## License

This project is licensed under the MIT License.

## Demo App

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://app-starter-kit.streamlit.app/)

## GitHub Codespaces

[![Open in GitHub Codespaces](https://github.com/codespaces/badge.svg)](https://codespaces.new/streamlit/app-starter-kit?quickstart=1)

