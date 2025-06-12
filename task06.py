text =  input("Matn kiriting: ")

counter = 0
for ch in text:
    if ch == ".":
        counter += 1

print(counter)