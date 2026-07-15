# Number Statistics
print("Number Statistics")
numbers = list(map(int, input("Please enter the 10 numbers (separated by space): ").split(" ")))

for index, number in enumerate (numbers, start=1):
    print(f"Number {index}: {number}")

avg = sum(numbers)/len(numbers)

print("Results: ")
print("Highest: ",max(numbers))
print("Lowest: ",min(numbers))
print("Average: ", avg)
print("Total: ",sum(numbers))