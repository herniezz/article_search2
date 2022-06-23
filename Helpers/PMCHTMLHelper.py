import requests
from bs4 import BeautifulSoup


class PMCHTMLHelper:

    def __init__(self, _url):
        self.url = _url
        self.htmlContent = self.__download_html_content()
        self.soup = BeautifulSoup(self.htmlContent, features="html.parser")

    def __download_html_content(self):
        response = requests.get(self.url, allow_redirects=True)

        if response.status_code == 200:
            htmlContent = response.content.decode("utf-8")

        return htmlContent

    def get_article_names_value(self):
        articles_names = []
        for article_name in self.soup.find_all('div', class_="title"):
            articles_names.append(article_name.getText(
                "#text").replace("#text", ""))

        return articles_names

    def get_href_value(self):
        href_arr = []
        last_value = ""
        for href in self.soup.find_all('a', class_="view"):
            href_value = href.get("href")
            if href_value == "#":
                continue

            if last_value[0:24] != href_value[0:24]:
                href_arr.append(f"https://www.ncbi.nlm.nih.gov{href_value}")

            last_value = href_value
        return href_arr

    def get_authors_name_value(self):
        authors_names = []
        for author_name in self.soup.find_all('div', class_="desc"):
            authors_names.append(author_name.getText(
                "#text").replace("#text", ""))

        return authors_names

    def get_doi_values(self):
        doi_arr = []
        for doi in self.soup.find_all('span', class_="doi"):
            doi_arr.append(doi.getText("#text").replace("#text", ""))

        return doi_arr

    def print_results(self):
        href_values = self.get_href_value()
        doi_values = self.get_doi_values()
        author_names = self.get_authors_name_value()
        for idx, article_name in enumerate(self.get_article_names_value()):
            print(f"\nArticle name: {article_name}")
            print(f"Authors: {author_names[idx]}")
            print(f"URL: {href_values[idx]}")
            print(f"DOI: {doi_values[idx]}")
