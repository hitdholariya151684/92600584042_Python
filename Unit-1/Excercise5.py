numbers = [1, 2, 3, 4, 5,6]

# Indexing
print(numbers[0])
print(numbers[2])

# Slicing
print(numbers[1:5])

# Add element
numbers.append(6)
print(numbers)

# List comprehension
square = [x*x for x in numbers]
print(square)
