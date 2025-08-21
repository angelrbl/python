def palindrome(word):
    isPalindrome = False
    word = word.lower().replace(" ", "")
    for char in range(0, len(word)):
        if word[char] == word[-(char+1)]:
            isPalindrome = True
            pass
        else:
            isPalindrome = False
            break
    return isPalindrome

def main():
    word = input("Write a word to check if it is a palindrome: ")
    print(f"Sorry, {word} is not a palindrome." if palindrome(word) == False else f"Yes, {word} is a palindrome!")

if __name__ == "__main__":
    main()
