import requests
from bs4 import BeautifulSoup



# HTMLHelper is an abstract for downloading and interpreting HTML files
# this one is dedicated to PubMed
# do naprawy - linki i articles

class PubMedHelper:
    def __init__(self, _url):
        self.url = _url
        self.htmlContent = self.__download_html_content()
        self.soup = BeautifulSoup(self.htmlContent, features="html.parser")

    def __download_html_content(self):
        response = requests.get(self.url, allow_redirects=True)

        if response.status_code == 200:
            htmlContent = response.content.decode("utf-8")

        return htmlContent

    def get_href_value(self):
        href_value = []
        for href in self.soup.find_all('a', class_ ="docsum-title"):
        href_value.append("https://pubmed.ncbi.nlm.nih.gov{}".format(href.get("title")))

        return href_value



    def get_article_name_value(self):
        articles_names = []
        for article_name in self.soup.find_all('a', class_="docsum-title"):
            articles_names.append("article_name: {}".format(article_name.getText("#text")).replace("#text", ""))

        return articles_names

    def get_authors_name_value(self):
        authors_names = []
        for author in self.soup.find_all('span', class_="docsum-authors full-authors"):
            authors_names.append(("authors_name:{}".format(author.getText("#text")).replace("#text", ""))

        return authors_names

    def get_doi_value(self):
        doi_value = []
        for doi in self.soup.find_all('span', class_="docsum-journal-citation full-journal-citation"):
            doi_value.append("doi:{}".format(doi.getText("#text")))

        return doi_value


