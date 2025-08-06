# Write a program that:

# 1. Asks the user how many people (n) to analyze (between 1 and 10).

# 2. For each person:
    # Ask for their name and age
    # Validate that the age is a valid integer between 1 and 120
    # Classify their age:
        # 0–12: Child
        # 13–17: Teen
        # 18–64: Adult
        # 65+: Senior
    # Track how many are in each group

# 3. After the loop, print:
    # Total number of users
    # Number of Children, Teens, Adults, Seniors
    # Average age of all users

child_sum = 0
teen_sum = 0
Adult_sum = 0
senior_sum = 0
users_age = []

try:
    n = int(input("How many People: "))
    
    if not 1 <= n <= 10:
        print("Out of range")  
    
    
    for i in range(n):
        name = input(f"\nName {i + 1}: ")

        while True:
            try:
                age = int(input("Age: "))

                if not 0 <= age <= 120:
                    print("Out of range")
                    continue

                users_age.append(age)

                if age <= 12:
                    child_sum += 1
                    print(f"{name} is a Child")
                elif 13 <= age <= 17:
                    teen_sum += 1
                    print(f"{name} is a Teen")
                elif 18 <= age <= 64:
                    Adult_sum += i
                    print(f"{name} is an Adult")
                else:
                    print(f"{name} is a Senior")

                break
            except ValueError:
                print("Invalid Input. Please enter a number.")
    average = sum(users_age) / len(users_age)
    
    print("\nAges entered:", users_age)
    print(f"\nNumber of users: {n}")
    print(f"Number of Children: {child_sum}")
    print(f"Number of Teens: {teen_sum}")
    print(f"Number of Adult: {Adult_sum}")
    print(f"Number of Seniors: {senior_sum}")
    print(f"Average age of all users is: {average}")    

except ValueError:
    print("Invalid Input")