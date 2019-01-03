import math

appliances = {
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

electricityPrice = {
  "00:00": 2,
  "00:30": 1.5,
  '0100': -1.11,
  "0130": -1.11,
  "0200": -1.43,
  "0230": -1.43,
  "0300": 1.69,
  "0330": 2.53,
  "0400": 5

}

def getHighestSumAddress(dictionary):
    highestAddress = sorted(dictionary.keys())[-1]
    nextHighestAddress = math.pow(2, math.log2(highestAddress) + 1) - 1
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
    totalUsage = int(input("What is your usage sum address? "))
    if totalUsage <= getHighestSumAddress(appliances):
        addresses = subsetsum(list(appliances.keys()), totalUsage)
        for pin in addresses:
            print("Turning on Pin {} with Description {} with address {}".format(appliances[pin][0], appliances[pin][1], pin))
    else:
        print("That sum address is invalid, the highest it can be is {}".format(getHighestSumAddress(appliances))
        main()


if __name__ == '__main__':
    main()
