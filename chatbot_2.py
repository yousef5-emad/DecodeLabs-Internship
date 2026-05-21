

import random  
import time    


GREETINGS_RESPONSES = [
    "Hey there!  Great to see you. What's on your mind?",
    "Hello! I'm ARIA, your AI assistant. How can I help you today?",
    "Hi! Hope you're having a great day. Ask me anything!",
    "Hey! Nice to meet you. I'm all ears ",
]

FAREWELL_RESPONSES = [
    "Goodbye! It was nice chatting with you. Take care! ",
    "See you later! Hope I was helpful. Bye! ",
    "Farewell! Come back anytime you need help. ",
    "Bye bye! Have a wonderful day ahead! ",
]

MOTIVATIONAL_QUOTES = [
    " 'The only way to do great work is to love what you do.' — Steve Jobs",
    " 'It does not matter how slowly you go as long as you do not stop.' — Confucius",
    " 'Believe you can and you're halfway there.' — Theodore Roosevelt",
    " 'Push yourself, because no one else is going to do it for you.'",
    " 'Dream big. Start small. Act now.'",
]

JOKES = [
    "Why do programmers prefer dark mode? Because light attracts bugs! ",
    "Why was the computer cold? Because it left its Windows open! ",
    "I told my computer I needed a break. Now it won't stop sending me Kit-Kat ads. ",
    "Why do Java developers wear glasses? Because they don't C#! ",
    "How many programmers does it take to change a light bulb? None — that's a hardware problem! ",
]

UNKNOWN_RESPONSES = [
    "Hmm, I'm not quite sure about that. Try asking something else! ",
    "That's a bit beyond me right now. Want to try a different question?",
    "I didn't quite catch that. Could you rephrase it? ",
    "Interesting... but I'm not sure how to answer that. Ask me something else!",
]



def greet_user():
    print("=" * 55)
    print("       Welcome to ARIA — Your AI Assistant ")
    print("=" * 55)
    print("  Type 'help' to see what I can do.")
    print("  Type 'exit', 'quit', or 'bye' to leave.")
    print("-" * 55)

  
    name = input("  Before we start — what's your name? ➤ ").strip()

    
    if not name:
        name = "Friend"

    
    name = name.capitalize()

    print(f"\n  Nice to meet you, {name}! I'm ARIA ")
    print("-" * 55 + "\n")

    return name   


#

def show_help():
    help_text = """
┌─────────────────────────────────────────────┐
│               ARIA — HELP MENU              │
├─────────────────────────────────────────────┤
│  👋 Say hi / hello / hey    → Greet me      │
│  😊 how are you             → My mood       │
│  🙋 what's your name        → Who am I      │
│  👨‍💻 who made you            → My developer  │
│  😂 tell me a joke          → A funny joke  │
│  💪 motivate me             → Inspiration   │
│  ❓ help                    → This menu     │
│  🚪 exit / quit / bye       → End chat      │
└─────────────────────────────────────────────┘
"""
    print(help_text)




def chatbot_response(user_input, name):

    # ── Greetings ──
    if any(word in user_input for word in ["hello", "hi", "hey", "howdy", "sup", "greetings"]):
        return random.choice(GREETINGS_RESPONSES)

    # ── How are you / feelings ──
    elif any(word in user_input for word in ["how are you", "how do you feel", "are you okay", "you good"]):
        return f"I'm doing great, {name}! Always ready to chat. How about you? "

    # ── User feeling good ──
    elif any(word in user_input for word in ["i'm good", "i am good", "doing well", "doing great", "i'm fine", "i'm okay"]):
        return f"That's awesome to hear, {name}! Keep that energy up! "

    # ── User feeling sad / bad ──
    elif any(word in user_input for word in ["i'm sad", "i am sad", "not good", "feeling bad", "i'm tired", "stressed", "bored"]):
        return f"Aww, I'm sorry to hear that, {name}.  Here's something to cheer you up — {random.choice(MOTIVATIONAL_QUOTES)}"

    # ── Chatbot's name ──
    elif any(word in user_input for word in ["your name", "what are you called", "who are you"]):
        return "I'm ARIA — Artificial Responsive Intelligence Assistant. Nice to meet you! "

    # ── Developer / creator ──
    elif any(word in user_input for word in ["who made you", "who created you", "your developer", "who built you", "your creator"]):
        return "I was built by yousef emad  Pretty cool, right? "

    # ── Joke request ──
    elif any(word in user_input for word in ["joke", "funny", "make me laugh", "tell me something funny"]):
        return random.choice(JOKES)

    # ── Motivation request ──
    elif any(word in user_input for word in ["motivate", "motivation", "inspire", "quote", "encourage"]):
        return random.choice(MOTIVATIONAL_QUOTES)

    # ── Help command ──
    elif "help" in user_input:
        show_help()
        return ""  

    # ── Thank you ──
    elif any(word in user_input for word in ["thank", "thanks", "thank you"]):
        return f"You're very welcome, {name}!  I'm always here if you need anything."

    
    elif any(word in user_input for word in ["what can you do", "capabilities", "features"]):
        show_help()
        return ""

   
    elif user_input == "":
        return "It looks like you didn't type anything. Try asking me something! "

   
    else:
        return random.choice(UNKNOWN_RESPONSES)




def exit_program(name):
    print("\n" + "-" * 55)
    print(f"  {random.choice(FAREWELL_RESPONSES)}")
    print(f"  Session ended. See you next time, {name}! ")
    print("=" * 55 + "\n")




def main():

   
    user_name = greet_user()

    
    while True:

        
        raw_input = input(f"  {user_name} ➤ ").strip().lower()

       
        if not raw_input:
            print("  ARIA ➤ You didn't type anything. I'm all ears! \n")
            continue   

        
        if raw_input in ["exit", "quit", "bye"]:
            exit_program(user_name)
            break  

     
        response = chatbot_response(raw_input, user_name)

        if response:
           
            time.sleep(0.3)
            print(f"  ARIA ➤ {response}\n")

if __name__ == "__main__":
    main()