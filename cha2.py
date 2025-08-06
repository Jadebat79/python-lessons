# Ask the user how many ports they want to check.
# For each port:
    # Ask for the port number.
    # Validate that the input is a valid integer.
    # Classify the port based on the number range.
    # Handle invalid port numbers and retry as needed.

# Print the classification result clearly.

try:
    ports = int(input("how many port do you want to classify? "))
except ValueError:
    print("Invalid input! Please enter a valid number.")
    exit()
    
for i in range(ports):
    while True:
        try:
            
                port = int(input(f"\nEnter port {i + 1}: "))

                if 0 <= port <= 1023:
                    print(f"{port} is a Well-known ports")
                elif 1024 <= port <= 49151:
                    print(f"{port} is a Registered ports")
                elif 49152 <= port <= 65535:
                    print(f"{port} is a Dynamic/private ports")
                else:
                    print(f"{port} is invalid")
        
                break
        except ValueError:
            print("Invalid input! Please enter a valid number.")