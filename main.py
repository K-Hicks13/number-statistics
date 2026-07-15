# Number Statistics
from Functions import average, maximum, minimum, total, enumerate_numbers, sort_numbers

print("Number Statistics")

while True:
    user_input = input("\nPlease enter 10 numbers separated by spaces: ")

    try:
        numbers = list(map(int, user_input.split()))

        if len(numbers) == 10:
            break

        print("Please enter exactly 10 numbers.")

    except ValueError:
        print("Please enter numbers only.")

enumerate_numbers(numbers)

print("\nResults: ")
print(f"Highest: {maximum(numbers)}")
print(f"Lowest: {minimum(numbers)}")
print(f"Average: {average(numbers):.2f}")
print(f"Total: {total(numbers)}")

print("\nNumbers sorted: ", sort_numbers(numbers))