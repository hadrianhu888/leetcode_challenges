

hexmap = {'0000': '0', '0001': '1', '0010': '2', '0011': '3', '0100': '4',
          '0101': '5', '0110': '6', '0111': '7', '1000': '8', '1001': '9',
          '1010': 'A', '1011': 'B', '1100': 'C', '1101': 'D', '1110': 'E',
          '1111': 'F'}


def hexmap():
    hexmap = {}
    for i in range(16):
        hexmap[bin(i)[2:].zfill(4)] = hex(i)[2:].upper()
    return hexmap


def binary2hex(binary):
    hex = ""
    for i in range(0, len(binary), 4):
        hex += hexmap[binary[i:i+4]]
    return hex


def main():
    binary = input("Enter a binary number: ")
    print("Hexadecimal number is: ", binary2hex(binary))


if __name__ == "__main__":
    main()
