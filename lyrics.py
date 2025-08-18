from bs4 import BeautifulSoup
import requests
import re

author: str = ""
song_name: str = ""

def scrape_lyrics():
    url = f"https://genius.com/{author}-{song_name}-lyrics"

    response = requests.get(url)
    doc = BeautifulSoup(response.text, "html.parser")
    lyrics_containers = doc.find("div", {"class": "Lyrics__Container-sc-a49d8432-1 fBKwZw"}).text

    lyrics = format_lyrics_1(lyrics_containers)
    lyrics = format_lyrics_2(lyrics)
    lyrics = add_new_line(lyrics)

    return lyrics


def format_lyrics_1(str):
    return re.sub(r"([\[])", r"\n\1", str)

def format_lyrics_2(str):
    return re.sub(r"([\]])", r"\1\n", str)

def add_new_line(str):
    return re.sub(r"([a-z])([A-Z])", r"\1\n\2", str)

if __name__ == "__main__":
    author = input("Please provide an author name: ").replace(" ", "-")
    song_name = input(f"Please provide a song written by {author}: ").replace(" ", "-")

    print(scrape_lyrics())