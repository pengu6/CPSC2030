import requests
from bs4 import BeautifulSoup
import pandas as pd

url =  'https://www.foxnews.com/'

response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")



headlines = []
for item in soup.find_all("h2", class_="headline"):
    headlines.append(item.text)

print(headlines)

categories = {"Sports": [], "Politics": [], "Tech": [], "Health": [], "World": []}

keywords = {
    "Sports": ["game", "match", "team", "score"],
    "Politics": ["election", "president", "government"],
    "Tech": ["AI", "technology", "software", "startup"],
    "World": ["isreal", "war", "russia","terrorism", "un"],
    "Health": ["virus", "death", "doctors", "hospital", "medical"]
}

for headline in headlines:
    for category, words in keywords.items():
        if any(word.lower() in headline.lower() for word in words):
            categories[category].append(headline)


df = {cat: pd.DataFrame(categories[cat], columns=["Headline"]) for cat in categories}
for cat, data in df.items():
    data.to_csv(f"{cat}_news.csv", index=False)

print("Categorized news saved!")