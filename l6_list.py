# A list is an ordered, changeable collection of items.

# Creating a list
fruits = ["apple", "banana", "cherry"]
mixed = [1, "hello", True]

# Accessing Element
print(fruits[1])
print(mixed[1])

# Adding & Removing Items
## Add
fruits.append("tomato") #append takes only one argument

## remove
mixed.remove("hello")

## Insert at index
fruits.insert(1, "mango") #this adds the value to a particular place

## Delete by index
del fruits[0]

# Looping Through a List
for fruit in fruits:
    print(fruit)

# indexing Through a List
for i in range(len(fruits)):
    print(f"{i}: {fruits[i]}")

# List of Numbers + Calculations
numbers =[1, 2, 3, 4]

total = sum(numbers)
average = sum(numbers) / len(numbers)
maximum = max(numbers)
minimum = min(numbers)

print(total)