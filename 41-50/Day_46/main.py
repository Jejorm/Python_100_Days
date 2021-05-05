from bs4 import BeautifulSoup
import requests
from pprint import pprint

date = input("Which year do you want to travel to? type the date in this format YYYY-MM-DD: ")

response = requests.get(f"https://www.billboard.com/charts/hot-100/{date}")


soup = BeautifulSoup(response.text, "html.parser")

songs_names_span = soup.select(".chart-element__information__song")

songs_names = [song.getText() for song in songs_names_span]

pprint(all_songs_list)
print(len(all_songs_list))
