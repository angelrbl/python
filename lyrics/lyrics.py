from bs4 import BeautifulSoup
import requests

author: str = ""
song_name: str = ""

def scrape_lyrics():
    url = f"https://genius.com/{author}-{song_name}-lyrics"

    response = requests.get(url)
    doc = BeautifulSoup(response.text, "html.parser")
    return doc.find("div", {"class": "Lyrics__Container-sc-a49d8432-1 fBKwZw"}).text.strip

if __name__ == "__main__":
    author = input("Please provide an author name: ")
    song_name = input(f"Please provide a song written by {author}: ")

    print(scrape_lyrics())