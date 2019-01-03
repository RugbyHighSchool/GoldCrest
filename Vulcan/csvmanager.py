import csv
from dateutil import parser
from datetime import datetime

class CSVParser:
    def __init__(self, filepath):
        self.filepath = filepath
        with open(self.filepath, newline='') as file:
            self.file = file
            self.dictionary = {}
            self.csvfile = csv.reader(self.file)
            for row in self.csvfile:
                self.dictionary[parser.parse(row[0])] = float(row[1])

    def printDictionary(self):
        for k, v in self.dictionary.items():
            print("{} : {}".format(k, v))

date = CSVParser('dateep.csv')
