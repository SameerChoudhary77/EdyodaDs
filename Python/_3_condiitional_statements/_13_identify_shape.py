# check the shape

length = int(input("Enter the length "))
breadth = int(input("Enter the breadth"))

if length==breadth and length !=0 and breadth != 0:
    print("The dimensions are of a square")
elif length == 0 and breadth == 0:
    print("The number is neutral")
else:
    print("The dimensions are of a rectangle")