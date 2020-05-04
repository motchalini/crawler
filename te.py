from scraper import Scraper

text = Scraper.get_html("https://www.google.com")
print(text.title.get_text())
