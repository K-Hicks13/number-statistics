def enumerate_numbers(numbers):
    for index, number in enumerate(numbers, start=1):
        print(f"Number {index}: {number}")

def maximum(numbers):
    return max(numbers)

def minimum(numbers):
    return min(numbers)

def average(numbers):
    return sum(numbers)/len(numbers)

def total(numbers):
    return sum(numbers)

def sort_numbers(numbers):
    return sorted(numbers)