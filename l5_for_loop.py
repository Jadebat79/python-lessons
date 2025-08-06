# Write a script that:

# Asks for a number n between 1 and 10
# Prints "Looping..." that many times, with the loop index shown:

n = int(input("Enter a number between 1 and 10: "))

if 1 <= n <= 10:
    for i in range(1, n + 1):
        print(f"Loop {i}")
else:
    print("Number is out of range")

# Variation 1: Only Even Numbers
n = int(input("Enter a number between 1 and 20: "))

if 1 <= n <= 20:
    for i in range(1, n + 1):
        if i % 2 == 0:
            print(i)
else:
    print("Number out of range")

# Variation 2: Only Odd Numbers
n = int(input("Enter a number between 1 and 20: "))

if 1 <= n <= 20:
    for i in range(1, n + 1):
        if i % 2 != 0:
            print(i)
else:
    print("Number out of range")

# Variation 3: operations of All Numbers
n = int(input("Enter a number between 1 and 20: "))

total = 0

if 1 <= n <= 20:
    for s in range(1, n + 1):
        total += s                      # sum 
        print(f"Sum of 1 to {n} is {total}")
        total -= s    #subtraction
        total *= s    #product
        
    
    average = total / n  # average of total

else:
    print("Number out of range")

# Sum of Even and Odd Separately
n = int(input("Enter a number betwwen 1 and 10: "))

even_sum = 0
odd_sum = 0

if 1<= n <= 10:
    for i in range(1, n + 1):
        if i % 2 == 1:
            even_sum += i
        else:
            odd_sum += i
    print(f"Sum of even numbers is {even_sum}")
    print(f"Sum of odd number is {odd_sum}")
else:
    print("Number out of range")

# Variation 5: Count of Even and Odd Numbers
n = int(input("Enter a number between 1 and 20: "))

even_count = 0
odd_count = 0

if 1 <= n <= 20:
    for i in range(1, n + 1):
        if i % 2 != 1:
            odd_count += 1
        else:
            even_count += 1
    print(f"Count of Odd numbers is {odd_count}")
    print(f"Count of Even numbers is {even_count}")

else:
    print("Number out of range")