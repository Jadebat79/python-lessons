# Write a program that:

# Creates a list of 5 numbers entered by the user.

# Then prints:
    # All numbers
    # The sum
    # The average
    # The largest and smallest number

# Bonus: Print which ones are even and odd

numbers = []

for i in range(5):
    while True:
        try:
            num = int(input(f"\nNumber is {i + 1}: "))
            numbers.append(num)
            break
        except ValueError:
            print("Invalid input. Please enter a valid integer.")

print("\nNumbers entered:", numbers)

total = sum(numbers)
print(total)

average = sum(numbers) / len(numbers)
print(average)

largest = max(numbers)
print(largest)

smallest = min(numbers)
print(smallest)