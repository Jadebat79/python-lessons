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

try: 
    n = int(input("How many People do you want to analyze (3-10): "))
    if not 3 <= n <= 10:
        print("Out of range")
        exit()

    for i in range(n):
        while True:
            try:
                num = int(input(f"\nEnter Number {i + 1}: "))
                numbers.append(num)

                if num % 2 == 0:
                    even_num += 1
                else:
                    odd_num += 1
                
                product *= num
                print(f"{num} squared is: {num ** 2}")

                break
            except ValueError:
                print("Enter valid integer")

    num_sum = sum(numbers)
    average = num_sum / len(numbers)
    minimum = min(numbers)
    maximum = max(numbers)

    print("\nNumbers entered:", numbers)
    print(f"Total even numbers: {even_num}")
    print(f"Total odd numbers: {odd_num}")
    print(f"Sum of numbers: {num_sum}")
    print(f"Average of numbers: {average}")
    print(f"Product of numbers: {product}")
    print(f"Minimum number: {minimum}")
    print(f"Maximum number: {maximum}")

except ValueError:
    print("Invalid input! Please enter a valid number.")
    exit()