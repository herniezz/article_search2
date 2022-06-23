import requests
from bs4 import BeautifulSoup


class DiVaHTMLHelper:

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
        for article_name in self.soup.find_all('a', class_="titleLink singleRow linkcolor"):
            articles_names.append(article_name.getText())

        return articles_names

    def get_href_value(self):
        href_value = []
        for href in self.soup.find_all('a', class_="titleLink singleRow linkcolor"):
            href_value.append(
                "http://www.diva-portal.org{}".format(href.get("href")))

        return href_value

    def get_authors_name_value(self):
        authors_names = []
        for author_name in self.soup.find_all('div', class_="ui-button-text ui-c"):
            if author_name.getText("#text") != "et al.":
                authors_names.append(author_name.getText(
                    "#text").replace("#text", ""))

        return authors_names

    def print_results(self):
        href_values = self.get_href_value()
        for idx, article_name in enumerate(self.get_article_names_value()):
            print(f"\nArticle name: {article_name}")
            print(f"URL: {href_values[idx]}")
