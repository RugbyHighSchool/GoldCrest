numbers = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512]
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
    compositeNumbers = subsetsum(numbers, 429)
    if compositeNumbers is not None:
        for pin in compositeNumbers:
            print("Turning On Pin {} which corresponds to {}".format(pins[pin], appliances[pins[pin]]))

if __name__ == '__main__':
    main()
