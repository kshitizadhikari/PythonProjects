from bs4 import BeautifulSoup
import requests
import csv


def main():
    url = "https://quotes.toscrape.com/"
    page_to_scrape = requests.get(url)
    soup = BeautifulSoup(page_to_scrape.text, "html.parser")
    quotes = soup.find_all("span", attrs={"class": "text"})
    authors = soup.find_all("small", attrs={"class": "author"})


    with open("scrappedData.csv", "w") as f:
        writer = csv.writer(f)
        writer.writerow(['Quote', 'Author'])
        
        for quote, author in zip(quotes, authors):
            writer.writerow([quote.text, author.text])
            print(f"{quote.text} - {author.text}")

if __name__ == '__main__':
    main()