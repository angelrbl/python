import json

file_name = 'hangman/words.json'
words = {}
valid_words = []

def load_values(file_name):
    try:
        with open(file_name, 'r') as f:
            return json.load(f)
    except:
        print("Cannot find a valid word list")

def choose_lang(words):
    lang = input("\nWhat language are you playing in? (en/es): ")
    match lang:
        case 'en':
            return [word for word in words.keys() if words.get(word) == 'en']
        case 'es':
            return [word for word in words.keys() if words.get(word) == 'es']
        case _:
            print("Invalid input, please try again: ")
            choose_lang(words)

def choose_dif(words):
    dif = input("\nHow difficult do you want the game to be? (easy/hard/all): ")
    match dif:
        case 'easy':
            return [word for word in words if len(word) <= 4]
        case 'hard':
            return [word for word in words if len(word) > 4]
        case 'all':
            return words
        case _:
            print("Invalid input, please try again: ")
            choose_dif(words)

def game_logic():
    ...

def main():
    valid_words = choose_lang(words)
    valid_words = choose_dif(valid_words)
    print(valid_words)

if __name__ == "__main__":
    words = load_values(file_name)
    main()