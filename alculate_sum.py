def calculate_sum(numbers):
    return sum(numbers)

def main():
    # Taking user input for a list of numbers
    numbers = [int(x) for x in input("Enter a list of numbers separated by space: ").split()]

    # Calculating the sum using the calculate_sum function
    result = calculate_sum(numbers)

    # Printing the result
    print(f"The sum of the elements in the list is: {result}")

if __name__ == "__main__":
    main()
