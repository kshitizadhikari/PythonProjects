from bs4 import BeautifulSoup
import requests
import csv

def main():
    url = "https://flixhq.to/home"
    page_to_scrape = requests.get(url)
    soup = BeautifulSoup(page_to_scrape.text, "html.parser")

    sections = soup.find_all("section", attrs={"class": "block_area block_area_home section-id-02"})

    for section in sections:
        heading = section.find("h2", attrs={"class": "cat-heading"})
        if heading.text == "Latest Movies":
            print(heading.text)
            block = section.find("div", attrs={"class": "film_list-wrap"})
            items = block.find_all("div", attrs={"class": "flw-item"})
            for item in items:
                detail = item.find("div", attrs={"class": "film-detail"})
                movie = detail.find("h3", attrs={"class": "film-name"})
                movie_name = movie.find("a")
                print(movie_name.text)
    # for category in categories:
    #     if category.text == "Latest Movies":
    # movies = soup.find_all("h3", attrs={"class": "film-name"})

    # for movie in movies:
    #     title = movie.find("a")
    #     print(title.text)


if __name__ == '__main__':
    main()