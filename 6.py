def remove_duplicates(input_string):
    # Convert the string to a set to remove duplicates, then join the characters back into a string
    result_string = ''.join(set(input_string))
    return result_string

def main():
    input_string = input("Enter a string: ")
    result = remove_duplicates(input_string)
    print(f"String after removing duplicates: {result}")

if __name__ == "__main__":
    main()
