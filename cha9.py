# Challenge: Port Range Analyzer
# 🎯 Your Task
# Write a Python program that:

# 1. Asks the user how many ports they want to check (between 3 and 10).

# 2. Takes each port number as input and stores it in a list.

# 3. Uses functions to:
    # Count how many are well-known ports (0–1023)
    # Count how many are registered ports (1024–49151)
    # Count how many are dynamic/private ports (49152–65535)
    # Find the lowest and highest port entered
    # Calculate the average port number

# 4. Prints a neat summary.

def well_known_ports(ports):
    count = 0
    for x in ports:
        if x <= 1023:
            count += 1
    return count

def registered_ports(ports):
    return sum(1 for x in ports if 1024 <= x <= 49151)

def private_ports(ports):
    return sum(1 for x in ports if 49152 <= x <= 65535)

def average_port(ports):
    if len(ports) == 0:
        return 0
    return sum(ports) / len(ports)

ports = []

try: 
    n = int(input("How many ports do you want to check (3-10): "))
    if not 3 <= n <= 10:
        print("Out of range")
        raise SystemExit
    
    for i in range(n):
        while True:
            try:
                port = int(input(f"\nEnter Port Number {i + 1}: "))
                ports.append(port)

                break
            except ValueError:
                print("Input is invalid. Please enter an integer.")
    

    wellknown = well_known_ports(ports)
    regis = registered_ports(ports)
    pri = private_ports(ports)
    avg = average_port(ports)
    mn = min(ports)
    mx = max(ports)

    print(f"\nPorts entered: {ports}")
    print(f"\nWell known ports is: {wellknown}")
    print(f"\nRegistered ports: {regis}")
    print(f"\nPrivates ports: {pri}")
    print(f"\nThe average port: {avg}")
    print(f"\nThe lowest port entered is: {mn}")
    print(f"\nThe highest port entered is: {mx}")

except ValueError:
    print("Top-level input was invalid. Please run again.")
