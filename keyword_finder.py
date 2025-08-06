
def main():
    find_word(get_text())

def get_text():
    return input("Please paste the text you want to find: ").split(' ')

def find_word(text):
    found = False
    keyword = input("Type the word you want to find: ").strip().lower()

    for word in text:
        if keyword == word:
            found = True
            print("Your word", keyword,"was found in this text! It is positioned in place:",text.index(word) + 1)
            again = input("Do you want to find another word? (y/n): ").strip().lower()
            if again == 'y':
                find_word(text)
            elif again == 'n':
                if input("Do you want to change to a new text? (y/n): ").strip().lower() == 'y':
                    find_word(get_text())
                else:    
                    break
            else:
                break
        else:
            pass
    if found == False:
        print('Your was not found in this text, try another word')
        find_word(text)
    
main()