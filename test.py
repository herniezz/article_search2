
import unittest
import requests
from Helpers import FileHelper
from Helpers import PubMedHelper
from Helpers import PMCHTMLHelper
from Helpers import SpringerHTMLHelper
from Helpers import DiVaHTMLHelper

#sprawdz czy jest zawartosc w htmlcontent

class testHtmlContent(unittest.TestCase):


    # pmc = PMCHTMLHelper.PMCHTMLHelper(fileHelper.urls[3])
    # springer = SpringerHTMLHelper.SpringerHTMLHelper(fileHelper.urls[6])
    # diva = DiVaHTMLHelper.DiVaHTMLHelper(fileHelper.urls[7])

    def testHtmlContent(self):
        fileHelper = FileHelper.FileHelper("urls.txt", "cognition")
        pubMed = PubMedHelper.PubMedHelper(fileHelper.urls[2])
        self.assertNotEqual(pubMed.htmlContent, "")

if __name__ == '__main__':
    unittest.main()
