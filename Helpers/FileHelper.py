# FileHelper class is a basic class used to read URLs from a file and
# replace a word to form a query

class FileHelper:

    def __init__(self, path, word):
        self.urls = []
        with open(path, 'r') as file:
            self.file_data = file.read()
            self.file_data = self.file_data.replace('{query}', word)
            self.urls = self.file_data.split("\n")
