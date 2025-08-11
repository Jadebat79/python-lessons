# Number Stats Analyzer
# 1. Ask the user for how many numbers they want to analyze (between 3 and 10).

# 2. Accept those numbers and store them in a list.

# 3. Then:
    # Print all the numbers
    # Print how many are even, how many are odd
    # Print the sum, average, product, maximum, and minimum
    # Print the square of each number

# Number Stats Analyzer
numbers = []
even_num = 0
odd_num = 0
product = 1

try: 
    # Ask for the number of entries
    print("Welcome to the Number Stats Analyzer!")
    n = int(input("How many People do you want to analyze (3-10): ")) 
    if not 3 <= n <= 10:
        print("Out of range") # Invalid input, exit the program
        exit()


    for i in range(n):
        while True:
            try:
                # Prompt for each number
                num = int(input(f"\nEnter Number {i + 1}: "))
                numbers.append(num)

                # Check if the number is even or odd
                if num % 2 == 0:
                    even_num += 1
                else:
                    odd_num += 1
                
                # Calculate the product
                product *= num
                
                # Print the square of the number
                print(f"{num} squared is: {num ** 2}")

                break  # Exit the inner loop if input is valid
            except ValueError:
                print("Enter valid integer") # Invalid input, prompt again

    # Calculate statistics
    num_sum = sum(numbers)
    average = num_sum / len(numbers)
    minimum = min(numbers)
    maximum = max(numbers)

    # Print the results
    print("\nNumbers entered:", numbers)
    print(f"Total even numbers: {even_num}")
    print(f"Total odd numbers: {odd_num}")
    print(f"Sum of numbers: {num_sum}")
    print(f"Average of numbers: {average}")
    print(f"Product of numbers: {product}")
    print(f"Minimum number: {minimum}")
    print(f"Maximum number: {maximum}")

except ValueError:
    print("Invalid input! Please enter a valid number.") # Invalid input, exit the program
    exit()

