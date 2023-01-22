num = int(input("Enter the number to check if it is divisible by 3 and 5 "))

if num % 3 == 0 and num % 5 == 0:
    print("Yes the number is divisible by 3 and 5")
elif num % 3 == 0:
    print("Num divisible by only 3")
elif num % 5 == 0:
    print("Num divisible by only 5")
else:
    print("Number not divisible by 3 and 5")


num = int(input("Enter the number to check if it is in range of 10-201 "))
if num >= 10 and num <= 201:
    print("It is in range")
else:
    print("It is not in range")