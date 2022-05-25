from Helpers import FileHelper
from Helpers import PubMedHelper
from Helpers import PMCHTMLHelper
from Helpers import SpringerHTMLHelper
from Helpers import DiVaHTMLHelper


print("hi there, this is a multi search engine for articles\nplease, write your keyword")
word = "cognition" # input the word

fh = FileHelper.FileHelper("urls.txt", word)
ph = PubMedHelper.PubMedHelper(fh.urls[2])
phh = PMCHTMLHelper.PMCHTMLHelper(fh.urls[3])
shh = SpringerHTMLHelper.SpringerHTMLHelper(fh.urls[6])
dhh = DiVaHTMLHelper.DiVaHTMLHelper(fh.urls[7])

#print(phh.get_href_value())
for idx, i in enumerate(shh.get_article_name_value()):
    print(i)

