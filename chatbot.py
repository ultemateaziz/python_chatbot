# Step 1: Install NLTK (Run this in a Colab cell)
!pip install nltk

# Step 2: Import Libraries and Download NLTK Data
import nltk
from nltk.chat.util import Chat, reflections

nltk.download('punkt')

# Step 3: Define the Chatbot's Responses
pairs = [
    [
        r"my name is (.*)",
        ["Hello %1, How are you today?",]
    ],
    [
        r"hi|hey|hello",
        ["Hello", "Hey there",]
    ],
    [
        r"what is your name?",
        ["I am a chatbot created by OpenAI.",]
    ],
    [
        r"how are you?",
        ["I'm doing good. How about you?",]
    ],
    [
        r"sorry (.*)",
        ["It's okay", "No problem",]
    ],
    [
        r"i'm (.*) doing good",
        ["Nice to hear that!", "Alright, great!",]
    ],
    [
        r"quit",
        ["Bye! Take care.", "Goodbye! It was nice talking to you."]
    ],
    [
        r"(.*)",
        ["I didn't understand that. Can you say it again?",]
    ],
]

# Step 4: Create the Chatbot
def chatbot():
    print("Hi! I'm your chatbot. Type 'quit' to exit.") 
    chat = Chat(pairs, reflections)
    chat.converse()

# Step 5: Run the Chatbot
chatbot()
