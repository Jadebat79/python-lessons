# Write a script that:

# Asks the user how many people they want to classify.
# For each person, it:
# Prompts for their name and age.
# Validates that the age is a valid number.
# Prints their age group:
# < 13: Child
# 13–17: Teen
# 18–64: Adult
# 65+: Senior

try:
    users = int(input("how many people do you want to classify? "))
except ValueError:
    print("Invalid input! Please enter a valid number.")
    exit()

for i in range(users):   
    name = input(f"\nUser Name is {i + 1}: ")
    
    while True:
        try:
            age = int(input("User age is: "))

            if age < 13:
                print(f"{name} is a Child")
            elif 13 <= age <= 17:
                print(f"{name} is a Teen")
            elif 18 <= age <=64:
                print(f"{name} is an Adult")
            elif age <= 65:
                print(f"{name} is a Senior")
            else:
                print("We are dealing with a Robot")
        
            break
        except ValueError:
            print("Invalid input! Please enter a valid number.")