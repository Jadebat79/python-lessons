try:
    age = int(input("Enter your age: "))

    if age < 13:
        print("Applicants is still a Child")
    elif 13 <= age < 18:
        print("Applicants is a Teen")
    elif 18 <= age < 65:
        print("Applicants is an Adult")
    elif age >= 65:
        print("Applicants is a Senior")
    else:
        print("Applicants is still not a human")

except ValueError:
    print("Invalid input! Please enter a valid number.")


# advanced version

while True:
    try:
        age = int(input("Enter your age: "))
        
        if age < 13:
            print("Applicant is still a Child")
        elif 13 <= age < 18:
            print("Applicant is a Teen")
        elif 18 <= age < 65:
            print("Applicant is an Adult")
        elif age >= 65:
            print("Applicant is a Senior")
        else:
            print("Applicant is still not a human")
        break
    except ValueError:
        print("Invalid input! Please enter a valid number.")


