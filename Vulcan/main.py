import math
from csvmanager import *
from datetime import datetime
import time

debug = True # i.e. not on a rpi
if not debug:
    from gpiozero import LED
    leds = {}

appliances = { # address, pin, description
  # Efficient appliances
  1: [2, "Efficient Fridge"],
  2: [3, "Efficient TV"],
  4: [4, "Efficient Dishwasher"],
  8: [5, "Efficient Washing Machine"],
  16: [6, "Efficient Water Heater"],
  # Inefficient appliances
  32: [10, "Inefficient Fridge"],
  64: [11, "Inefficient TV"],
  128: [12, "Inefficient Dishwasher"],
  256: [13, "Inefficient Washing Machine"],
  512: [14, "Inefficient Water Heater"]
}

def getHighestSumAddress(dictionary):
    highestAddress = sorted(dictionary.keys())[-1] # gets the highest current address
    nextHighestAddress = math.pow(2, math.log2(highestAddress) + 1) - 1 # as the next highest address will be a power of 2 higher as that is how they sum.
    return nextHighestAddress

def subsetsum(array,num):
    if num == 0 or num < 1:
        return None
    elif len(array) == 0:
        return None
    else:
        if array[0] == num:
            return [array[0]]
        else:
            with_v = subsetsum(array[1:], (num - array[0]))
            if with_v:
                return [array[0]] + with_v
            else:
                return subsetsum(array[1:],num)

def main():
    usageData = DatePriceUsage('datawithusage.csv')
    if not debug:
        for address in appliances.keys():
            leds[address] = LED(appliances.values()[0])

    while True:
        for timestamp, priceandusage in usageData.dictionary.items():
            if priceandusage[1] <= getHighestSumAddress(appliances):
                addresses = subsetsum(list(appliances.keys()), priceandusage[1])
                for address in addresses:
                    print("At time {} Turning on Pin {} which is {}".format(timestamp, appliances[address][0], appliances[address][1]))
                    # turn on the pin
                    if not debug:
                        leds[address].on()
                time.sleep(2)

if __name__ == '__main__':
    main()
