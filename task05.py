text = input("Matn kiriting: ")

text01 = ''
for i in range(len(text)-1,-1,-1):
    text01 += text[i]

print(text01)