age = int(input("Enter your age: "))

if age < 13:
    print("Applicants is still a Child")
elif 13 <= age < 18:
    print("Applicants is a Teen")
elif 18 <= age < 64:
    print("Applicants is an Adult")
elif age >= 65:
    print("Applicants is a Senior")
else:
    print("Applicants is still not a human")