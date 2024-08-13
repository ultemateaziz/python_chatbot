
# Interactive Speech-Enabled Chatbot

This project is a simple yet interactive chatbot that leverages speech recognition and text-to-speech capabilities to provide a more natural and engaging user experience. Built using Python, this chatbot can listen to user queries, process them, and respond both via text and speech.

#Features





## Features

- Speech Recognition: Captures user input through the microphone and converts it into text using Google's Speech Recognition API.
- Text-to-Speech: Converts the bot's text responses into speech, allowing for more interactive communication.
- NLP-Based Responses: Uses the NLTK library to handle user queries and provide appropriate responses.
- Conversational Flow: Predefined response pairs to handle common conversational patterns.


## Getting Started

### Prerequisites

To run this project locally, you need to have Python installed along with the following Python packages:

- SpeechRecognition
- pyttsx3
- pyaudio
- nltk

## Running Tests

To run tests, run the following command

```bash
  pip install SpeechRecognition pyttsx3 pyaudio nltk
```
## Setup to usage

Download NLTK Data:

```bash
import nltk
nltk.download('punkt')
```
Run the chatbot python application

```bash
python chatbot.py
```
Example Interaction

```bash
Bot: Hi! I'm your chatbot. Say 'quit' to exit.
Listening...
You said: Hello
Bot: Hello
Listening...
You said: What is your name?
Bot: I am a chatbot created by OpenAI.
```

## Important Notes
Local Environment: This project is designed to run on your local machine due to the requirement for microphone access. 

Running this in an environment like Google Colab might not work as intended.
Dependencies: Ensure all dependencies are properly installed in your local environment.
