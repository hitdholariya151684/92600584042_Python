f = open("sample.txt", "w+")
f.write("Hello Python")

print("Position:", f.tell())

f.seek(0)
print("Position after seek:", f.tell())

print("Data:", f.read(5))
print("Current position:", f.tell())

f.close()
