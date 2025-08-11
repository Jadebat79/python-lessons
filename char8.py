# Challenge: Number Stats Using Functions
# 🎯 Your Task
# Write a program that:

# 1. Asks the user how many numbers they want to analyze (between 3 and 10).
# 2. Takes the numbers as input and stores them in a list.
# 3. Uses functions to:
    # Get the sum of the list
    # Get the average of the list
    # Get the product of the list
    # Count how many numbers are even
    # Count how many numbers are odd
    # Print the square of each number


# Solutions
def is_even(num):
    return num % 2 == 0
                
def square(num):
    return num ** 2
                
def product_of_list(numbers):
    product = 1
    for num in numbers:
        product *= num
    return product
                
def sum_of_list(numbers):
    return sum(numbers)
                
def average_of_list(numbers):
    if len(numbers) == 0:
        return 0
    return sum(numbers) / len(numbers)

def even_count(numbers):
    count = 0
    for x in numbers:
        if x % 2 == 0:
            count += 1
    return count

def odd_count(numbers):
    return sum(1 for x in numbers if x % 2 != 0)


numbers = []


try:
    print("Welcome to the Number Stats Functions Analyzer!")
    n = int(input("How many numbers do you want to analyze (3-10): "))
    if not 3 <= n <= 10:
        print("Out of range")
        raise SystemExit

    for i in range(n):
        while True:
            try:
                num = int(input(f"\nEnter Number {i + 1}: "))
                numbers.append(num)
                break
            except ValueError:
                print("Input invalid")

    
    total = sum_of_list(numbers)
    avg = average_of_list(numbers)
    prod = product_of_list(numbers)
    evens = even_count(numbers)
    odds = odd_count(numbers)
    mn = min(numbers)
    mx = max(numbers)


except ValueError:
    print("Out of range")

                
                
