

def dec2hex(dec):
    """Convert decimal to hexadecimal."""
    hex = ""
    while dec > 0:
        hex = "0123456789ABCDEF"[dec % 16] + hex
        dec = dec // 16
    return hex


def main():
    dec = int(input("Enter a decimal number: "))
    print("Hexadecimal number is: ", dec2hex(dec))


if __name__ == "__main__":
    main()
