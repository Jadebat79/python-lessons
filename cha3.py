# 🧩 Mini Challenge: Mark Even and Odd Numbers
# 🧱 Task:
# Ask the user for a number n between 1 and 20.
    # Loop from 1 to n (inclusive).
    # # For each number, print:
    # # "X is Even" if the number is even
    # # "X is Odd" if the number is odd

n = int(input("Enter a number between 1 and 20: "))

if 1 <= n <= 20:
    for i in range(1, n + 1):
        if i % 2 == 0:
            print(f"{i} is Even")
        else:
            print(f"{i} is Odd")
else:
    print("Number out of range")