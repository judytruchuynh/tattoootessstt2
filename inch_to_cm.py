def inch_to_cm(inch):
    return inch * 2.54

if __name__ == "__main__":
    inch = float(input("Enter length in inches: "))
    cm = inch_to_cm(inch)
    print(f"{inch} inches is equal to {cm} centimeters.")
