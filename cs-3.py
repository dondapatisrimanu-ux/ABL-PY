def number_triangle(n):
    for i in range(1, n + 1):
        for j in range(1, i + 1):
            print(j, end=" ")
        print()
def inverted_triangle(n):
    for i in range(n, 0, -1):
        for j in range(1, i + 1):
            print(j, end=" ")
        print()
def floyds_triangle(n):
    num = 1
    for i in range(1, n + 1):
        for j in range(i):
            print(num, end=" ")
            num += 1
        print()
def number_pyramid(n):
    for i in range(1, n + 1):
        print(" " * (n - i), end="")
        for j in range(1, i + 1):
            print(j, end=" ")
        print()
def pascals_triangle(n):
    for i in range(n):
        print(" " * (n - i), end="")
        value = 1
        for j in range(i + 1):
            print(value, end=" ")
            value = value * (i - j) // (j + 1) if j < i else 1
        print()
def main():
    while True:
        print("\nADVANCED NUMERIC PATTERN GENERATOR")
        print("1. Number Triangle")
        print("2. Inverted Number Triangle")
        print("3. Floyd's Triangle")
        print("4. Number Pyramid")
        print("5. Pascal's Triangle")
        print("6. Exit")
        choice = input("Enter your choice (1-6): ")
        if choice == "6":
            print("Program terminated.")
            break
        if choice not in {"1", "2", "3", "4", "5"}:
            print("Invalid choice. Please select 1-6.")
            continue
        try:
            rows = int(input("Enter the number of rows (1-20): "))
            if not 1 <= rows <= 20:
                print("Please enter a number between 1 and 20.")
                continue
        except ValueError:
            print("Invalid input. Enter a whole number.")
            continue
        if choice == "1":
            number_triangle(rows)
        elif choice == "2":
            inverted_triangle(rows)
        elif choice == "3":
            floyds_triangle(rows)
        elif choice == "4":
            number_pyramid(rows)
        elif choice == "5":
            pascals_triangle(rows)
if __name__ == "__main__":
    main()