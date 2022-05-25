import requests
from bs4 import BeautifulSoup

# HTMLHelper is an abstract for downloading and interpreting HTML files.
# This one is dedicated to springer site.
# to repair href

class SpringerHTMLHelper:
    def __init__(self, _url):
        self.url = _url
        self.htmlContent = self.__download_html_content()
        self.soup = BeautifulSoup(self.htmlContent, features="html.parser")

    def __download_html_content(self):
        response = requests.get(self.url, allow_redirects=True)

        if response.status_code == 200:
            htmlContent = response.content.decode("utf-8")

        return htmlContent

    def get_article_name_value(self):
        articles_names = []
        for article_name in self.soup.find_all('a', class_="title"):
            articles_names.append(article_name.getText("#text").replace("#text", ""))

        return articles_names

    def get_href_value(self):
        href_value = []
        for href in self.soup.find_all('a', class_="title"):
            href_value.append("https://link.springer.com/search?query={}".format(href.get("title")))

        return href_value

    def get_authors_name_value(self):
        authors_names = []
        for author_name in self.soup.find_all('a', class_="authors"):
            authors_names.append(author_name.getText("#text").replace("#text", "").strip())

        return authors_names