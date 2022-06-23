from Helpers import FileHelper
from Helpers import PubMedHelper
from Helpers import PMCHTMLHelper
from Helpers import SpringerHTMLHelper
from Helpers import DiVaHTMLHelper

print("Multisearch engine for articles")
print("Please, write your keyword")

word = input()
print("Please, wait...")

fileHelper = FileHelper.FileHelper("urls.txt", word)
pubMed = PubMedHelper.PubMedHelper(fileHelper.urls[2])
pmc = PMCHTMLHelper.PMCHTMLHelper(fileHelper.urls[3])
springer = SpringerHTMLHelper.SpringerHTMLHelper(fileHelper.urls[6])
diva = DiVaHTMLHelper.DiVaHTMLHelper(fileHelper.urls[7])

print("\n\n\n\n~~ PUBMED ~~:")
pubMed.print_results()
print("\n\n\n\n~~ PMC ~~:")
pmc.print_results()
print("\n\n\n\n~~ SPRINGER ~~:")
springer.print_results()
print("\n\n\n\n~~ DIVA ~~:")
diva.print_results()
