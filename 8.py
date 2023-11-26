def create_tuples_with_cube(numbers):
    result_tuples = [(num, num**3) for num in numbers]
    return result_tuples

def main():
    # Taking user input for a list of numbers
    numbers = [int(x) for x in input("Enter a list of numbers separated by space: ").split()]

    # Creating tuples with the number and its cube using the create_tuples_with_cube function
    result_tuples = create_tuples_with_cube(numbers)

    # Printing the result
    print("Tuples with number and its cube:")
    for tpl in result_tuples:
        print(tpl)

if __name__ == "__main__":
    main()
