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
0000:  2,
0030:  1.5,
0100:  -1.11,
0130:  -1.11,
0200:  -1.43,
0230:  -1.43,
0300:  1.69,
0330:  2.53,
0400:  5,
0430:  9.5,
0500:  25.14,
0:30:  27,
06:00:  35,
06:30:  38.52,
07:00:  44,
07:30:  44.49,
08:00:  39,
08:30:  38.28,
09:00:  34.11,
09:30:  34,
10:00:  34.5,
10:30:  34.5,
11:00:  36,
11:30:  35.82,
12:00:  35,
12:30:  35,
13:00:  35.12,
13:30:  34.42,
14:00:  29.99,
14:30:  29.8,
15:00:  36,
15:30:  40.62,
16:00:  39.64,
16:30:  39.89,
17:00:  48,
17:30:  48,
18:00:  50.8,
18:30:  50.65,
19:00:  52.5,
19:30:  52.65,
20:00:  56.5,
20:30:  55,
21:00:  50,
21:30:  47,
22:00:  46,
22:30:  44.5,
23:00:  34.79,
23:30:  32.79
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
