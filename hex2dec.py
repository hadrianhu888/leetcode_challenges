

def hex2dec(hexadecimal):
    """Convert hexadecimal to decimal."""
    decimal = 0
    for i in range(len(hexadecimal)):
        decimal = decimal * 16 + "0123456789ABCDEF".index(hexadecimal[i])
    return decimal

def main():
    hexadecimal = input("Enter a hexadecimal number: ")
    print("Decimal number is: ", hex2dec(hexadecimal))

if __name__ == "__main__":
    main()

    