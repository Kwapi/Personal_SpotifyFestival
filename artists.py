# get list of artists from opener website
import requests
from bs4 import BeautifulSoup

def getOpenerArtists():

    # Make a GET request to the webpage
    url = 'https://opener.pl/en/line-up-2023'
    response = requests.get(url)

    # Parse the HTML content of the webpage using BeautifulSoup
    soup = BeautifulSoup(response.content, 'html.parser')

    # Find all the <li> elements with class 'list-artist-item'
    artist_list_items = soup.find_all('li', class_='list-artist-item')

    # Extract the artist names from the <div> elements with class 'title' in each <li> element
    artists = [item.find('div', class_='title').text for item in artist_list_items]

    return artists

def getArtistsFromFile():
    with open('artists.txt', 'r') as file:
        data = file.readlines()

    # Remove new line character and trailing whitespaces
    artistsList= [line.strip() for line in data]