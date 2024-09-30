# main.py

import mood_response

def main():
    mood = input("How are you feeling today? ")
    response = mood_response.get_mood_response(mood)
    print(response)

if __name__ == "__main__":
    main()
