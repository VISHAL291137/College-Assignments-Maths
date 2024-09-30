def find_hcf(x, y):
    while y:
        x, y = y, x % y
    return x

def find_lcm(x, y):
    lcm = (x * y) // find_hcf(x, y)
    return lcm

def main():
    num1 = int(input("Enter the first number: "))
    num2 = int(input("Enter the second number: "))

    hcf = find_hcf(num1, num2)
    lcm = find_lcm(num1, num2)

    print(f"The HCF of {num1} and {num2} is: {hcf}")
    print(f"The LCM of {num1} and {num2} is: {lcm}")

if __name__ == "__main__":
    main()
