import random
import datetime

print("=== Welcome to AsharBot! 🤖 ===")
print("Type 'bye' or 'exit' anytime to end the chat.\n")

hour = datetime.datetime.now().hour
if hour < 12:
    print("AsharBot: Good morning! ")
elif hour < 18:
    print("AsharBot: Good afternoon! ")
else:
    print("AsharBot: Good evening! ")

print("AsharBot: How are you today?\n")

greetings = ["hello", "hi", "hey", "good morning", "good evening"]
how_are_you = ["how are you", "how r u", "hows it going"]
feeling_good = ["good", "great", "fine", "awesome", "fantastic"]
feeling_bad = ["sad", "tired", "not good", "bad", "upset"]

joke_triggers = ["tell me a joke", "say a joke", "make me laugh"]
jokes = [
"Why did the programmer quit his job? Because he didnt get arrays (a raise)! ",
    "Why do Java developers wear glasses? Because hey dont C#! ",
    "Whats a computers favorite snack? Microchips!" ,
    "Why did the programmer quit his job? Because he didntt get arrays (a raise)! ",
   "Why do Java developers wear glasses? Because they dont C#! ",
   "Whats a computers favorite snack? Microchips! ",
   "Why was the computer cold? It left its Windows open!" ,
    "Why did the computer go to therapy? It had too many bytes! ",
   "Why do programmers prefer dark mode? Because light attracts bugs! ",
    "Why did the function break up with the loop? Too many arguments! ",
    "Why do Python programmers have low self-esteem? They constantly compare themselves to others. ",
    "Why was the JavaScript developer sad? Because he didnt Node how to Express himself. ",
    "Why did the programmer bring a ladder to work? Because he was climbing the stack! ",
    "Why do programmers hate nature? Too many bugs. ",
    "Why did the developer go broke? Because he used up all his cache. ",
    "Why did the programmer drown? He tried to float() in a sea of exceptions. ",
    "Why did the database administrator leave his wife? She had one-to-many relationships. ",
    "Why did the web developer walk out of the restaurant? Because he didnt get arrays. ",
    "Why did the computer keep sneezing? It had a bad case of viruses! ",
    "Why was the developer unhappy at his job? He wanted arrays (a raise)! ",
    "Why do Java programmers wear glasses? Because they cant C#! ",
    "Why do coders always mix up Halloween and Christmas? Because Oct 31 == Dec 25! ",
    "Why did the programmer get kicked out of school? He kept taking classes. ",
    "Why did the computer go on a diet? It had too many bytes! ",
    "Why did the programmer cross the road? To debug the chicken. ",
    "Why do Python developers wear glasses? Because they dont see sharp. ",
    "Why was the function feeling depressed? Because it didnt return anything. ",
    "Why do programmers prefer iOS development? Less kernel panic. ",
    "Why do programmers hate socializing? Too many conflicts. ",
    "Why was the software developer always calm? Because he handled exceptions. ",
    "Why did the coder get stuck in the shower? He read the shampoo instructions: Lather, Rinse, Repeat… forever! ",
    "Why did the computer break up with the internet? There was too much buffering. ",
    "Why did the programmer go broke? Because he used up all his cache. ",
    "Why was the computer tired when it got home? It had too many tabs open! ",
    "Why did the software engineer stay at work late? He wanted to catch some bugs. ",
    "Why did the coder go broke? Because he lost his domain in a bet. ",
    "Why did the computer get glasses? To improve its web sight. ",
    "Why did the programmer get stuck on the elevator? Because he couldnt find the exit command.",
    "Why do programmers love coffee? Because it helps them Java better! ",
    "Why did the developer get locked out of his house? He forgot the key-value pair. ",
    "Why do programmers always mix up Christmas and Halloween? Oct 31 == Dec 25! ",
    "Why did the coder keep pressing F5? He wanted to refresh his life. ",
    "Why did the developer go broke? Because he cleared his cache. ",
    "Why did the computer get cold at work? Too many fans running. ",
    "Why did the JavaScript developer leave? Because he didnt get a callback. ",
    "Why did the programmer bring a ladder? To reach the high-level language. ",
    "Why do Python programmers prefer snakes? They avoid the bugs. ",
    "Why did the programmer quit his job? He didnt get arrays (a raise)! ",
    "Why did the HTML developer go broke? Because he kept using divs. ",
    "Why was the computer always calm? It had a lot of cache. ",
    "Why did the programmer write bad code? He didnt get the memo. ",
    "Why do coders hate commas? Because they always cause syntax errors. , ",
    "Why did the function fail its test? It didnt return the right value. ",
    "Why do developers hate office politics? Too many loops and conditions. ",
    "Why did the computer keep freezing? It left its Windows open. ",
    "Why did the coder get arrested? He was caught trying to break the loop. "
]

bot_name_triggers = ["your name", "who are you", "what are you"]
bot_name_responses = [
    "I'm AsharBot — your friendly chat companion!",
    "You can call me AsharBot ",
    "I'm just a program with a big heart"
]

time_triggers = ["time", "what time", "current time"]
weather_triggers = ["weather", "temperature", "rain"]
thanks_triggers = ["thanks", "thank you", "thx"]
bye_triggers = ["bye", "exit", "quit", "goodbye"]

while True:
    user = input("You: ").lower().strip()

    if not user:
        continue

    if user in bye_triggers:
        print("AsharBot: It was nice chatting with you! Take care ")
        break

    elif any(word in user for word in greetings):
        print(random.choice([
            "AsharBot: Hey there!",
            "AsharBot: Hello! Hows your day going?",
            "AsharBot: Hi! Nice to see you "
        ]))

    elif any(phrase in user for phrase in how_are_you):
        print(random.choice([
            "AsharBot: I'm just code, but I feel awesome when chatting with you!",
            "AsharBot: Doing great, thanks for asking! How about you?",
            "AsharBot: Im fantastic — ready to chat!"
        ]))

    elif any(word in user for word in feeling_good):
        print(random.choice([
            "AsharBot: Thats great to hear! Keep smiling ",
            "AsharBot: Awesome! Positive vibes only ",
            "AsharBot: Glad to know youre feeling good!"
        ]))
    elif any(word in user for word in feeling_bad):
        print(random.choice([
            "AsharBot: Im sorry to hear that. Want to talk about it?",
            "AsharBot: Bad days happen… but tomorrow will be better ",
            "AsharBot: Sending you a virtual hug "
        ]))

    elif any(trigger in user for trigger in joke_triggers):
        print("AsharBot:", random.choice(jokes))

    elif "my name is" in user:
        name = user.split("my name is")[-1].strip().title()
        print(f"AsharBot: Nice to meet you, {name}! ")
    elif "your name" in user or "who are you" in user:
        print("AsharBot:", random.choice(bot_name_responses))

    
    elif any(word in user for word in time_triggers):
        current_time = datetime.datetime.now().strftime("%I:%M %p")
        print(f"AsharBot: The current time is {current_time} ")

    elif any(word in user for word in weather_triggers):
        print("AsharBot: I cant check live weather yet, but its always sunny in Pythonland ")

    elif any(word in user for word in thanks_triggers):
        print("AsharBot: Youre welcome! ")

    else:
        print(random.choice([
            "AsharBot: Hmm… Im not sure I understand ",
            "AsharBot: Interesting! Tell me more.",
            "AsharBot: Lets talk about something fun! What’s your favorite hobby?",
            "AsharBot: Im still learning! Could you say that differently?"

        ]))
