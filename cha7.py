# Number Stats Analyzer
# 1. Ask the user for how many numbers they want to analyze (between 3 and 10).

# 2. Accept those numbers and store them in a list.

# 3. Then:
    # Print all the numbers
    # Print how many are even, how many are odd
    # Print the sum, average, product, maximum, and minimum
    # Print the square of each number

numbers = []
even_num = 0
odd_num = 0
product = 1

n = int(input("How many People do you want to analyze: "))

for i in range(n):
    while True:
        try:
            num = int(input(f"\nNumbers is {i + 1}: "))
            numbers.append(num)

            if num % 2 == 0:
                even_num += 1
            else:
                odd_num += 1
            
            print(f"squared: {i ** 2}")

            break
        except ValueError:
            print("Enter valid integer")

num_sum = sum(numbers)
average = sum(numbers) / len(numbers)
minimum = min(numbers)
maximum = max(numbers)

print()