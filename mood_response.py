# mood_response.py

def get_mood_response(mood):
    mood_responses = {
        "happy": "That's great to hear! Keep smiling! 😊",
        "sad": "I'm sorry to hear that. I hope things get better soon. 💙",
        "angry": "It's okay to feel angry sometimes. Take a deep breath. 🧘",
        "excited": "Awesome! What's got you so excited? 🎉",
        "nervous": "It's natural to feel nervous. You've got this! 💪",
        "tired": "Make sure to get some rest. You deserve it. 😴",
        "bored": "Maybe try something new to spice things up! 🎨"
    }
    return mood_responses.get(mood.lower(), "I'm not sure how to respond to that mood, but I hope you have a good day!")
