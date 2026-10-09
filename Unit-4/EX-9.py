# Write mode
f = open("data.txt", "w")
f.write("Hello Python")
f.close()

# Read mode
f = open("data.txt", "r")
print(f.read())
f.close()

# Append mode
f = open("data.txt", "a")
f.write("\nWelcome")
f.close()
