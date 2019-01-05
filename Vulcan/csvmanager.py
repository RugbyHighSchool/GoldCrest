import csv
from datetime import datetime

dateTimeParse = '%H:%M:%S'

class DatePrice:
    def __init__(self, filepath):
        with open(filepath, newline='') as file:
            self.dictionary = {}
            self.csvfile = csv.reader(file)
            for row in self.csvfile:
                if len(row) == 2: # Date and Price
                    self.dictionary[datetime.strptime(row[0], dateTimeParse)] = float(row[1])

    def printDictionary(self):
        for k, v in self.dictionary.items():
            print("{} : {} (£/MWhr) : {} (Pence/KWhr)".format(k, v, v / 10))

    def getLowestPrice(self):
        lowest = min(self.dictionary, key = self.dictionary.get)
        return { lowest : self.dictionary[lowest] }

class DatePriceUsage:
    def __init__(self, filepath):
        with open(filepath, newline='') as file:
            self.dictionary = {}
            self.csvfile = csv.reader(file)
            for row in self.csvfile:
                if len(row) == 3: # Date, Price and Usage
                    self.dictionary[datetime.strptime(row[0], dateTimeParse)] = [float(row[1]), int(row[2])]

    def printDictionary(self):
        for k, v in self.dictionary.items():
            print("{} : {} (£/MWhr) : {} (Pence/KWhr) : {} Usage Address".format(k, v[0], v[0] / 10, v[1]))
