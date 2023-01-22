# Logical operator

no1 = 10
no2 = 20

and_demo = no1 > 5 and no1 < no2
print("And: ", and_demo)

and_demo = no1 > 5 and no1 > no2
print("And: ", and_demo)

or_demo = no1 > 5 or no1 < no2
print("Or :",or_demo)

or_demo = no1 > 50 or no1 < no2
print("Or :",or_demo)

not_demo = not(no1 > no2)
print("not: ",not_demo)

or_demo = no1 > 50 or no1 < no2 and no1 == 10
print("Or :",or_demo)