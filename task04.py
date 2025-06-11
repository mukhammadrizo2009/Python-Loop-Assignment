import random

number = random.randint(1,20)

while True:
    result = int(input("1-20 gacha son kiriting: "))
    
    if result == number:
        print("Topding!")
        break
else:
    print("Qayta urining!")
        
