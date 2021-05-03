from bs4 import BeautifulSoup
import requests
from pprint import pprint

response = requests.get("https://news.ycombinator.com/news")

yc_webpage = response.text

soup = BeautifulSoup(yc_webpage, "html.parser")
# print(soup.title)

article_tag = soup.select_one(".storylink")
# article_tag = soup.find(name="a", class_="storylink")  # Alternative 

article_text = article_tag.getText()
article_link = article_tag.get("href")
article_upvote = soup.select_one(".score").getText()
# article_upvote = soup.find(name="span", class_="score").getText()  # Alternative

# print(article_text, article_link, article_upvote, sep="\n")


# # Get highest score news

articles = soup.select(".storylink")
# articles = soup.findall(name="a", class_="storylink")  # Alternative 

article_texts = []
article_links = []

for article in articles:
    text = article.getText()
    link = article.get("href")

    article_texts.append(text)
    article_links.append(link)


article_upvotes = []
subtexts = soup.select(".subtext")

for subtext in subtexts:
    # Check if a news has not score, in that case has 0 points.
    if subtext.select(".score") == []:
        article_upvotes.append(0)
    else:
        article_upvotes.append(int(subtext.select_one(".score").getText().split()[0]))


highest_rated = max(article_upvotes)
highest_rated_index = article_upvotes.index(highest_rated)

print(article_texts[highest_rated_index])
print(article_links[highest_rated_index], "\n")
print(highest_rated)
