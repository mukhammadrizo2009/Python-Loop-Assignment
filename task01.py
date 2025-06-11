text = input("Matn kiriting: ")

letter = "a,o,e,i,o,u"

hisob = 0

for i in text:
    if i in letter:
        hisob += 1
        result = hisob
print(f"Harflar soni:",result)