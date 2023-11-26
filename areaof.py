import math

def main():
    print("Choose a shape to calculate the area:")
    print("1. Circle")
    print("2. Rectangle")
    print("3. Square")

    choice = int(input("Enter your choice (1/2/3): "))

    if choice == 1:
        radius = float(input("Enter the radius of the circle: "))
        area = math.pi * radius**2
        print(f"The area of the circle is: {area:.2f}")
    elif choice == 2:
        length = float(input("Enter the length of the rectangle: "))
        width = float(input("Enter the width of the rectangle: "))
        area = length * width
        print(f"The area of the rectangle is: {area:.2f}")
    elif choice == 3:
        side = float(input("Enter the side length of the square: "))
        area = side**2
        print(f"The area of the square is: {area:.2f}")
    else:
        print("Invalid choice. Please enter 1, 2, or 3.")

if __name__ == "__main__":
    main()
