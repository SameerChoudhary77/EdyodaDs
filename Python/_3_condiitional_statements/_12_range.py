# Check if number is in range between 10-2-1

num = int(input("Enter the number to check if it is in range of 10-201 "))
if num >= 10 and num <= 201:
    print("Number is in range 10-201")
else:
    print("Number is not in range 10-201")

num = int(input("Enter the number "))
if num in range(10,201):
    print("num is in range")
else:
    print("'num is out of range")