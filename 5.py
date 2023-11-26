def count_vowels(input_string):
    vowels = set("aeiouAEIOU")  # Creating a set of vowels

    # Using a set intersection to find common elements (vowels) in the input string
    vowel_count = len(set(input_string) & vowels)

    return vowel_count

def main():
    input_string = input("Enter a string: ")
    result = count_vowels(input_string)
    print(f"Number of vowels in the string: {result}")

if __name__ == "__main__":
    main()
