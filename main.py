from prime.generator import prime_generator


def generate_prime():
    try:
        start = int(input("Enter range start: "))
        end = int(input("Enter range end: "))

        print("The prime numbers found in the range are:")
        for p in prime_generator(start, end):
            print(p)

        print("\n")
    except ValueError:
        print("Oops! Please enter a valid integer.\n")


print("Welcome to the Interactive Prime Number Generator!")

while True:
    print("\nEnter choice: ")
    print("=======================")
    print("Generate prime numbers: P")
    print("Exit: Q")

    choice = input().upper()

    if choice == "P":
        generate_prime()
    elif choice == "Q":
        print("The end.")
        break
    else:
        print("Invalid choice. Please enter again.")
