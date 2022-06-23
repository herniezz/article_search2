 # Article class is an abstract to save information about one article

class Article:
    def __init__(self, _name, _author, _doi, _url, _download):
        self.name_of_article = _name
        self.authors_name = _author
        self.doi = _doi
        self.url = _url
        self.download = _download