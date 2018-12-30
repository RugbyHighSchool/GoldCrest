numbers = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512]
pins = {
  1: 2,
  2: 3,
  4: 3,
  8: 4,
  16: 5,
  32: 10,
  64: 11,
  128: 12,
  256: 13,
  512: 14
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
            with_v = subsetsum(array[1:],(num - array[0]))
            if with_v:
                return [array[0]] + with_v
            else:
                return subsetsum(array[1:],num)

def main():
    ref = subsetsum(numbers, 125)
    if ref is not None:
        for pin in ref:
            print("Turning On Pin {}".format(pins[pin]))


if __name__ == '__main__':
    main()
