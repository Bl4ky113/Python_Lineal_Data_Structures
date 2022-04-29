
def pyramid_number (lower, upper, margin=0):
    spaces = " " * margin
    print(spaces, lower, upper)

    if lower > upper:
        print(spaces, 0)
        return 0
    else:
        result = lower + pyramid_number(lower + 1, upper, margin + 4)
        print(spaces, result)
        return result

def main ():
    pyramid_number(0, 5)

if __name__ == "__main__":
    main()
