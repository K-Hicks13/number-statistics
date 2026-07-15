# Number Statistics
from Functions import average, maximum, minimum, total, enumerate_numbers, sort_numbers

print("Number Statistics")
numbers = list(map(int, input("\nPlease enter the 10 numbers (separated by space): ").split(" ")))

enumerate_numbers(numbers)

avg = sum(numbers)/len(numbers)

print("\nResults: ")
print("Highest: ", maximum(numbers))
print("Lowest: ",minimum(numbers))
print("Average: ", average(numbers))
print("Total: ",total(numbers))

print("\nNumbers sorted: ", sort_numbers(numbers))