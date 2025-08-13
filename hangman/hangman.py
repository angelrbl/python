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

def choose_lang():
    lang = input("\nWhat language are you playing in? (en/es): ")
    match lang:
        case 'en':
            select_lang(words, "en")
        case 'es':
            select_lang(words, "es")
        case _:
            print("Invalid input, please try again: ")
            choose_lang()

def select_lang(words, lang):
    for word in words.keys():
        if words.get(word) == lang:
            valid_words.append(word)


def choose_dif():
    dif = input("\nHow difficult do you want the game to be? (easy/hard/all): ")
    match dif:
        case 'easy':
            return select_dif(valid_words, 'e')
        case 'hard':
            return select_dif(valid_words, 'h')
        case 'all':
            pass
        case _:
            print("Invalid input, please try again: ")
            choose_dif()

def select_dif(words, dif):
    for word in words:
        if len(word) > 4:
            words.remove(word)
        if len(word) < 4:
            words.remove(word)
    return words

def game_logic():
    ...

def main():
    choose_lang()
    global valid_words
    valid_words = choose_dif()
    print(valid_words)

if __name__ == "__main__":
    words = load_values(file_name)
    main()