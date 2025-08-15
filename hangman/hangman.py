import json
import random
from sys import exit

file_name = 'hangman/words.json'
words = {}
valid_words = []
max_strikes: int = 0

def load_values(file_name):
    try:
        with open(file_name, 'r') as f:
            return json.load(f)
    except:
        print("Cannot find a valid word list, please provide one.")
        exit(0)


def choose_lang(words):
    lang = input("\nWhat language are you playing in? (en/es): ")
    match lang:
        case 'en':
            return [word for word in words.keys() if words.get(word) == 'en']
        case 'es':
            return [word for word in words.keys() if words.get(word) == 'es']
        case _:
            print("Invalid input.")
            main()

def choose_dif(words):
    dif = input("How difficult do you want the game to be? (easy/normal/hard): ")
    match dif:
        case 'easy':
            return [word for word in words if len(word) <= 4], 7
        case 'normal':
            return words, 6
        case 'hard':
            return [word for word in words if len(word) > 4], 5
        case _:
            print("Invalid input.")
            main()

def game_logic(words, max_strikes):
    guess = []
    used_chars = []
    word = list(words[random.randint(0, len(words)-1)])
    strikes = 0

    for char in word:
        guess.append('_')

    print("\nYOUR WORD IS:")
    print(" ".join(guess), end='\n\n')

    while word != guess or strikes <= max_strikes:
        correct = False
        guesschar = input("Type one letter to guess: ")
        used_chars.append(guesschar)
        for i, char in enumerate(word):
            if char == guesschar:
                guess[i] = guesschar
                correct = True
        if correct == False:
            strikes += 1
        if strikes >= max_strikes:
            print(f"Sorry, but you reach the limit of {max_strikes} strikes, you lost.")
            strikes += 1
            main()
        if word == guess:
            strikes = max_strikes + 1
        print(f'{" ".join(guess)}   Strikes: {strikes}/{max_strikes}  Letters tried: {" ".join(used_chars)}\n')
    
    print(f"CONGRATULATIONS, YOU WON!! THE WORD WAS {"".join(word).upper()}. GOING BACK...")
    main()

def close():
    exit("Alright, see you soon!")


def choose_settings():
    global valid_words
    global max_strikes
    valid_words = choose_lang(words)
    valid_words, max_strikes = choose_dif(valid_words)
    main()

def main():
    
    print("\nHANGMAN:")
    print("[1] Play")
    print("[2] Change language & difficulty")
    print("[0] Exit")

    action = input("What do you want to do?: ")

    match action:
        case "1":
            game_logic(valid_words, max_strikes)
        case "2":
            choose_settings()
        case "0":
            close()
        case _:
            print("Invalid input, try again")
            main()

if __name__ == "__main__":
    words = load_values(file_name)
    choose_settings()
