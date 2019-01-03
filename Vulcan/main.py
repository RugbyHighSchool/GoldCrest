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
  256: [13, "Inefficient Washing Machine",
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
    for time, price in electricityPrice.items():
        print("Time {} with Price {}".format(time, price))
    compositeNumbers = subsetsum(list(pins.keys()), 429)
    if compositeNumbers is not None:
        for pin in compositeNumbers:
            print("Turning On Pin {} which corresponds to {}".format(pins[pin], appliances[pins[pin]]))

if __name__ == '__main__':
    main()
