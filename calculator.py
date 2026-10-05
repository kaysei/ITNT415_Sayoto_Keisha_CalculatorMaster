def add(a, b):
    return round(a + b, 10)

def subtract(a, b):
    return round(a - b, 10)


def multiply(a, b):
    return round(a * b, 10)


def divide(a, b):
    return a / b


def get_number(prompt):
    while True:
        value = input(prompt).strip()
        try:
            return float(value)
        except ValueError:
            print("Invalid input. Please enter a valid number.")


def show_menu():
    print("\n===== Calculator Master =====")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Exit")


def main():
    while True:
        show_menu()
        choice = input("Choose an option (1-5): ").strip()
        if choice == "5":
            print("Goodbye!")
            break
        if choice not in ("1", "2", "3", "4"):
            print("Invalid choice. Please select 1 to 5.")
            continue
        a = get_number("Enter first number: ")
        b = get_number("Enter second number: ")
        if choice == "1":
            print(f"Result: {add(a, b)}")
        elif choice == "2":
            print(f"Result: {subtract(a, b)}")
        elif choice == "3":
            print(f"Result: {multiply(a, b)}")
        elif choice == "4":
            print(f"Result: {divide(a, b)}")


if __name__ == "__main__":
    main()
