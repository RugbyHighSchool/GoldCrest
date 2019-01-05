import csv
from datetime import datetime

dateTimeParse = '%d/%m/%Y %H:%M:%S'

class CSVParser:
    def __init__(self, filepath):
        with open(filepath, newline='') as file:
            self.dictionary = {}
            self.csvfile = csv.reader(file)
            for row in self.csvfile:
                if len(row) == 2: # Date and Price
                    self.dictionary[datetime.strptime(row[0], dateTimeParse)] = float(row[1])

                if len(row) == 3: # Date, Price and Usage
                    self.dictionary[datetime.strptime(row[0], dateTimeParse)] = [float(row[1]), int(row[2])]

    def printDictionary(self):
        for k, v in self.dictionary.items():
            print("{} : {} (£/MWhr) : {} (Pence/KWhr)".format(k, v[0], v[0] / 10))

    def getLowestPrice(self):
        lowest = min(self.dictionary, key = self.dictionary.get)
        return { lowest : self.dictionary[lowest] }
