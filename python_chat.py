import re
import random
import nltk
nltk.download('punkt')

# Predefined intents and responses
intents = {
    "greeting": ["Hello!", "Hi there!", "Hey! How can I help you?"],
    "goodbye": ["Bye!", "See you soon!", "Take care!"],
    "thanks": ["You're welcome!", "No problem!", "Glad to help!"],
    "help": ["I can help you with movie suggestions, weather, or small talk."],
    "weather": ["It's sunny today!", "Looks like it might rain.", "I can't check real weather, but I hope it's nice!"],
    "movie": ["I recommend watching Inception!", "How about The Matrix?", "Try watching Interstellar!"],
    "fallback": ["Sorry, I didn't understand that.", "Can you rephrase it?"]
}

patterns = {
    "greeting": r"hello|hi|hey",
    "goodbye": r"bye|see you|goodbye",
    "thanks": r"thanks|thank you",
    "help": r"help|assist|support",
    "weather": r"weather|rain|sunny|forecast",
    "movie": r"movie|film|cinema|suggest.*movie|movie.*suggest"
}

# Chatbot engine
def get_intent(user_input):
    for intent, pattern in patterns.items():
        if re.search(pattern, user_input.lower()):
            return intent
    return "fallback"

def respond(user_input):
    intent = get_intent(user_input)
    return random.choice(intents[intent])

# Run chatbot
print("Chatbot: Hello! Type 'bye' to end the chat.")
while True:
    user_input = input("You: ")
    if user_input.lower() in ['bye', 'exit', 'quit']:
        print("Chatbot:", random.choice(intents["goodbye"]))
        break
    print("Chatbot:", respond(user_input))
