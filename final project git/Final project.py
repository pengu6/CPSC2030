import requests
from bs4 import BeautifulSoup
import pandas as pd
from abc import ABC, abstractmethod 
import csv

class BaseScraper(ABC):    
    @abstractmethod
    def fetch_data(self, url: str):
        pass

    @abstractmethod
    def parse_data(self, html: str):
        pass

class NewsScraper(BaseScraper):
    
    def fetch_data(self, url: str):
        response = requests.get(url)
        return response.text if response.status_code == 200 else None

    def parse_data(self, html: str):
        soup = BeautifulSoup(html, "html.parser")
        articles = []
        
        for item in soup.find_all("div", class_="article"):
            title = item.find("h2").text
            link = item.find("a")["href"]
            articles.append(Article(title, link))
        
        return articles

class Article:    
    def __init__(self, title: str, url: str):
        self.title = title
        self.url = url

    def __str__(self):
        return f"{self.title} ({self.url})"


class Category:
    
    def __init__(self, name: str):
        self.name = name
        self.articles = []

    def add_article(self, article: Article):
        self.articles.append(article)

class Categorizer:
    def __init__(self):
        self.categories = {
            "Sports": ["game", "team", "match"],
            "Politics": ["election", "government"],
            "Technology": ["AI", "software", "startup"]
        }
    def categorize(self, article: Article):
        for category, keywords in self.categories.items():
            if any(keyword.lower() in article.title.lower() for keyword in keywords):
                return category
        return "Uncategorized"

class CSVExporter:    
    def save(self, articles, filename="output.csv"):
        with open(filename, "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["Title", "URL"])
            for article in articles:
                writer.writerow([article.title, article.url])
        print("Data saved to", filename)

class ScraperManager:    
    def __init__(self):
        self.scrapers = []

    def add_scraper(self, scraper: BaseScraper):
        self.scrapers.append(scraper)

    def run_scrapers(self):
        for scraper in self.scrapers:
            url = "https://www.foxnews.com/"
            html = scraper.fetch_data(url)
            if html:
                articles = scraper.parse_data(html)
                for article in articles:
                    print(article)


scraper = NewsScraper()
manager = ScraperManager()
manager.add_scraper(scraper)
manager.run_scrapers()

'''url =  'https://www.foxnews.com/'

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

print("Categorized news saved!")'''