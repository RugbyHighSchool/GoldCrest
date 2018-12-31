pins = {
  # good appliances
  1: 2,
  2: 3,
  4: 4,
  8: 5,
  16: 6,
  # bad appliances
  32: 10,
  64: 11,
  128: 12,
  256: 13,
  512: 14
}

appliances = {
    2: "Good Fridge",
    3: "Good TV",
    4: "Good Dishwasher",
    5: "Good Washing Machine",
    6: "Good Water Heater",
    10: "Bad Fridge",
    11: "Bad TV",
    12: "Bad Dishwasher",
    13: "Bad Washing Machine",
    14: "Bad Water Heater"
}

electricityPrice = {
  0000: 2,
  0030: 1.5,
  0100: -1.11,
  0130: -1.11,
  0200: -1.43,
  0230: -1.43,
  0300: 1.69,
  0330: 2.53,
  0400: 5,
  0430: 9.5,
  0500: 25.14,
  0530: 27,
  0600: 35,
  0630: 38.52,
  0700: 44,
  0730: 44.49,
  0800: 39,
  0830: 38.28,
  0900: 34.11,
  0930: 34,
  1000: 34.5,
  1030: 34.5,
  1100: 36,
  1130: 35.82,
  1200: 35,
  1230: 35,
  1300: 35.12,
  1330: 34.42,
  1400: 29.99,
  1430: 29.8,
  1500: 36,
  1530: 40.62,
  1600: 39.64,
  1630: 39.89,
  1700: 48,
  1730: 48,
  1800: 50.8,
  1830: 50.65,
  1900: 52.5,
  1930: 52.65,
  2000: 56.5,
  2030: 55,
  2100: 50,
  2130: 47,
  2200: 46,
  2230: 44.5,
  2300: 34.79,
  2330: 32.79
}

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
    for price in electrictyPrice:
        print(price)
    compositeNumbers = subsetsum(list(pins.keys()), 429)
    if compositeNumbers is not None:
        for pin in compositeNumbers:
            print("Turning On Pin {} which corresponds to {}".format(pins[pin], appliances[pins[pin]]))

if __name__ == '__main__':
    main()
