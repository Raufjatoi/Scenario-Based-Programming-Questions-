# 8. Basic Customer Service Chatbot:
#Develop a program to simulate a simple chatbot for a customer service application. It should be able to:
# Greet users and understand their basic inquiries through natural language processing.
# Provide answers to frequently asked questions based on a predefined knowledge base.
# Offer basic troubleshooting steps for common issues.

import random

faq = {
    "What are your hours?": "We are open Monday to Friday, 9am to 5pm.",
    "How can I reset my password?": "You can reset your password by visiting our website and clicking on the 'Forgot Password' link.",
    "How do I contact support?": "You can contact support by emailing support@example.com or calling 1-800-123-4567.",
    "I'm having trouble logging in.": "Please make sure you are using the correct username and password. If you continue to have trouble, contact support.",
    "How long does shipping take?": "Shipping times vary depending on your location. Please check our website for estimated shipping times.",
    "Do you offer refunds?": "Yes, we offer refunds within 30 days of purchase. Please see our refund policy on our website for more details."
}

greetings = ["hi", "hello", "hey", "howdy", "hola"]
goodbyes = ["bye", "goodbye", "see you later", "adios"]
random_responses = ["I'm sorry, I'm not sure I understand.", "Could you please rephrase that?", "Let me check on that for you."]

def greet_user():
    print("Hello! How can I help you today?")

def chatbot():
    greet_user()
    while True:
        user_input = input("> ").strip().lower()

        if user_input in goodbyes:
            print("Goodbye! Have a great day.")
            break
        elif user_input in greetings:
            print('Hello there! How can I assist you?')
        else:
            response = faq.get(user_input, random.choice(random_responses))
            print(response)

def main():
    chatbot()

if __name__ == "__main__":
    main()
