import csv
from datetime import datetime

dateTimeParse = '%d/%m/%Y %H:%M:%S'

class CSVParser:
    def __init__(self, filepath):
        with open(filepath, newline='') as file:
            self.dictionary = {}
            self.csvfile = csv.reader(file)
            for row in self.csvfile:
                self.dictionary[datetime.strptime(row[0], dateTimeParse)] = float(row[1])

    def printDictionary(self):
        for k, v in self.dictionary.items():
            print("{} : {} (£/MWhr) : {} (Pence/KWhr)".format(k, v, v / 10))

    def getLowestPrice(self):
        lowest = min(self.dictionary, key = self.dictionary.get)
        return { lowest : self.dictionary[lowest] }
