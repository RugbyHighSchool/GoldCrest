import csv
from datetime import time, datetime

class CSVParser:
    def __init__(self, filepath):
        self.filepath = filepath
        with open(self.filepath, newline='') as file:
            self.file = file
            self.dictionary = {}
            self.csvfile = csv.reader(self.file)
            for row in self.csvfile:
                print(length(row[0]))
                dataTime = row[0].split(":")
                self.dictionary[time(int(dataTime[0]), int(dataTime[1]), 0)] = float(row[1])

x = CSVParser('dateelectricityprice.csv')

for k, v in x.dictionary.items():
#    print('{:%H:%M} with Price £{} per MWHr'.format(k, v))
