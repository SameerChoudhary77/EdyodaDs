#practice sum#
# Take input from user and check if it is even number or odde number

num = int(input("Enter the number:"))
if num % 2==0:
    print("The number is an even number: ",num)
elif num == 0:
    print("The number is neutral")
else:
    print("The number is an odd number",num)