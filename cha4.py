# Number Analyzer
# 🎯 Your Task
# Write a Python script that:

# Asks the user for a number n between 1 and 20.
    # If n is not within that range, print "Out of range" and exit.
# Otherwise, for each number from 1 to n:
    # Print whether the number is even or odd
    # Print its square

# After the loop, print:
    # The sum of all numbers from 1 to n
    # The average of the numbers
    # The product of the numbers
    # The count of even and odd numbers



try:
    n = int(input("Enter number between 1 and 20: "))
    
    if not 1 <= n <= 20:
        print("out of range")
        exit()
    
    total_sum = 0
    product = 1
    even_count = 0
    odd_count =0


    for i in range(1, n + 1):
            total_sum += i
            product *= i

            if i % 2 == 0:
                even_count += 1
                print(f"{i} is even")
            else:
                odd_count += 1
                print(f"{i} is odd")
            
            print(f"{i} squared is {i ** 2}")  
            

    average = total_sum / n    
            
    print(f"Sum of 1 to {n} is: {total_sum}")
    print(f"The product of 1 to {n} is: {product}")
    print(f"The average of the sum total is: {average}")
    print(f"Total odd numbers is {odd_count}")
    print(f"Total even numbers is {even_count}")

except ValueError:  
    print("invalid, please enter a number")
    exit() 