import requests
from bs4 import BeautifulSoup


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
        for href in self.soup.find_all('a', class_="docsum-title"):
            href_value.append(
                "https://pubmed.ncbi.nlm.nih.gov{}".format(href.get("href")))

        return href_value

    def get_article_names_value(self):
        articles_names = []
        for article_name in self.soup.find_all('a', class_="docsum-title"):
            articles_names.append(article_name.getText().lstrip().rstrip())

        return articles_names

    def get_authors_name_value(self):
        authors_names = []
        for author in self.soup.find_all('span', class_="docsum-authors full-authors"):
            authors_names.append(author.getText("#text"))

        return authors_names

    def get_doi_values(self):
        doi_value = []
        for doi in self.soup.find_all('span', class_="docsum-journal-citation full-journal-citation"):
            doi_value.append("doi:{}".format(doi.getText("#text")))

        return doi_value

    def print_results(self):
        href_values = self.get_href_value()
        doi_values = self.get_doi_values()
        author_names = self.get_authors_name_value()
        for idx, article_name in enumerate(self.get_article_names_value()):
            print(f"\nArticle name: {article_name}")
            print(f"Authors: {author_names[idx]}")
            print(f"URL: {href_values[idx]}")
            print(f"DOI: {doi_values[idx]}")
