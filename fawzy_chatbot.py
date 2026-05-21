

import random
import time


from rich.console import Console
from rich.text import Text


console = Console()



GREETINGS_RESPONSES = [
    "Hey there! Great to see you. What's on your mind?",
    "Hello! I'm Fawzy, your AI assistant. How can I help you today?",
    "Hi! Hope you're having a great day. Ask me anything!",
    "Hey! Nice to meet you. I'm all ears.",
]

FAREWELL_RESPONSES = [
    "Goodbye! It was nice chatting with you. Take care!",
    "See you later! Hope I was helpful. Bye!",
    "Farewell! Come back anytime you need help.",
    "Bye bye! Have a wonderful day ahead!",
]

MOTIVATIONAL_QUOTES = [
    "'The only way to do great work is to love what you do.' — Steve Jobs",
    "'It does not matter how slowly you go as long as you do not stop.' — Confucius",
    "'Believe you can and you're halfway there.' — Theodore Roosevelt",
    "'Push yourself, because no one else is going to do it for you.'",
    "'Dream big. Start small. Act now.'",
]

JOKES = [
    "Why do programmers prefer dark mode? Because light attracts bugs!",
    "Why was the computer cold? Because it left its Windows open!",
    "I told my computer I needed a break. Now it won't stop sending me Kit-Kat ads.",
    "Why do Java developers wear glasses? Because they don't C#!",
    "How many programmers does it take to change a light bulb? None — that's a hardware problem!",
]

UNKNOWN_RESPONSES = [
    "Hmm, I'm not quite sure about that. Try asking something else!",
    "That's a bit beyond me right now. Want to try a different question?",
    "I didn't quite catch that. Could you rephrase it?",
    "Interesting... but I'm not sure how to answer that. Ask me something else!",
]




def bot_print(message):
    console.print(f"  [bold cyan]Fawzy :[/bold cyan] [cyan]{message}[/cyan]")




def greet_user():
    console.print()
    # Top separator line in yellow
    console.print(f"  [yellow]{'=' * 55}[/yellow]")
    # Welcome title in bold white
    console.print("  [bold white]     Welcome to Fawzy — Your AI Assistant[/bold white]")
    # Project credit line in dim white
    console.print("  [dim white]     Task created by Yousef Emad[/dim white]")
    console.print(f"  [yellow]{'=' * 55}[/yellow]")
    console.print("  [dim]Type 'help' to see what I can do.[/dim]")
    console.print("  [dim]Type 'exit', 'quit', or 'bye' to leave.[/dim]")
    console.print(f"  [yellow]{'-' * 55}[/yellow]")

    # Ask for the user's name using Rich prompt styling
    console.print("  [bold yellow]Before we start — what's your name?[/bold yellow] ", end="")
    name = input().strip()

   
    if not name:
        name = "Friend"

    # Capitalize name nicely
    name = name.capitalize()

    console.print(f"\n  [bold cyan]Nice to meet you, {name}! I'm Fawzy.[/bold cyan]")
    console.print(f"  [yellow]{'-' * 55}[/yellow]\n")

    return name


# ─────────────────────────────────────────────
#  FUNCTION: show_help()
#  Prints the help menu with green color.
# ─────────────────────────────────────────────

def show_help():
    # Print each line of the help menu in green
    console.print()
    console.print("  [green]┌─────────────────────────────────────────────[/green]")
    console.print("  [green]│[/green]  [bold green]          Fawzy — HELP MENU               [/bold green][green][/green]")
    console.print("  [green]├─────────────────────────────────────────────[/green]")
    console.print("  [green]│[/green]  [green]👋 Say hi / hello / hey    → Greet me      [/green][green][/green]")
    console.print("  [green]│[/green]  [green]😊 how are you             → My mood       [/green][green][/green]")
    console.print("  [green]│[/green]  [green]🙋 what's your name        → Who am I      [/green][green][/green]")
    console.print("  [green]│[/green]  [green]👨‍💻 who made you            → My developer  [/green][green][/green]")
    console.print("  [green]│[/green]  [green]😂 tell me a joke          → A funny joke  [/green][green][/green]")
    console.print("  [green]│[/green]  [green]💪 motivate me             → Inspiration   [/green][green][/green]")
    console.print("  [green]│[/green]  [green]❓ help                    → This menu     [/green][green][/green]")
    console.print("  [green]│[/green]  [green]🚪 exit / quit / bye       → End chat      [/green][green][/green]")
    console.print("  [green]└─────────────────────────────────────────────[/green]")
    console.print()




def chatbot_response(user_input, name):

    # ── Greetings ──
    if any(word in user_input for word in ["hello", "hi", "hey", "howdy", "sup", "greetings"]):
        return random.choice(GREETINGS_RESPONSES)

    # ── How are you / feelings ──
    elif any(word in user_input for word in ["how are you", "how do you feel", "are you okay", "you good"]):
        return f"I'm doing great, {name}! Always ready to chat. How about you?"

    # ── User feeling good ──
    elif any(word in user_input for word in ["i'm good", "i am good", "doing well", "doing great", "i'm fine", "i'm okay"]):
        return f"That's awesome to hear, {name}! Keep that energy up!"

    # ── User feeling sad / bad ──
    elif any(word in user_input for word in ["i'm sad", "i am sad", "not good", "feeling bad", "i'm tired", "stressed", "bored"]):
        return f"Aww, I'm sorry to hear that, {name}. Here's something to cheer you up — {random.choice(MOTIVATIONAL_QUOTES)}"

    # ── Chatbot's name ──
    elif any(word in user_input for word in ["your name", "what are you called", "who are you"]):
        return "I'm Fawzy, your AI assistant. Nice to meet you!"

    # ── Developer / creator ──
    elif any(word in user_input for word in ["who made you", "who created you", "your developer", "who built you", "your creator"]):
        return "This Ai was created by Yousef Emad."

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
        return f"You're very welcome, {name}! I'm always here if you need anything."

    # ── What can you do ──
    elif any(word in user_input for word in ["what can you do", "capabilities", "features"]):
        show_help()
        return ""

    # ── Empty input safety net ──
    elif user_input == "":
        return "It looks like you didn't type anything. Try asking me something!"

    # ── Unknown / unrecognized input ──
    else:
        return random.choice(UNKNOWN_RESPONSES)




def exit_program(name):
    console.print(f"\n  [yellow]{'-' * 55}[/yellow]")
    console.print(f"  [cyan]{random.choice(FAREWELL_RESPONSES)}[/cyan]")
    console.print(f"  [bold cyan]Session ended. See you next time, {name}![/bold cyan]")
    console.print(f"  [yellow]{'=' * 55}[/yellow]\n")




def main():

  
    user_name = greet_user()

   
    while True:

        
        console.print(f"  [bold yellow]{user_name} :[/bold yellow] ", end="")
        raw_input = input().strip().lower()

        # ── Handle completely empty input ──
        if not raw_input:
            bot_print("You didn't type anything. I'm all ears!")
            console.print()
            continue

        # ── Check for exit keywords ──
        if raw_input in ["exit", "quit", "bye"]:
            exit_program(user_name)
            break

        # ── Get and print chatbot response ──
        response = chatbot_response(raw_input, user_name)

        if response:
            time.sleep(0.3)   # Small pause for a natural feel
            bot_print(response)
            console.print()


# ─────────────────────────────────────────────
#  ENTRY POINT
# ─────────────────────────────────────────────

if __name__ == "__main__":
    main()
