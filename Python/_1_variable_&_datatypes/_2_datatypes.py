#datatype


num = 10
num_type = type(num)
print("Num Type:",num_type)

name = "Bharati"
name_type = type(name)
print("Name Type:",name_type)

salary = 10000.50
salary_type = type(salary)
print("Salary Type:",salary_type)

qualified = True
qualified_type = type(qualified)
print("Qualified Type:",qualified_type)

eq = 1 + 1j
eq_type = type(eq)
print("Equation Type:",eq_type)

future_idea = None
future_idea_type = type(future_idea)
print("Future Idea Type:",future_idea_type)


#Collection
#list
#tuple
#dict
#set

student_names = ["ram","raj","sita","gita","rohit"]
print(student_names)
print(student_names[3])

student_names = ["ram","raj","sita","gita","rohit",78,90.6,True]
print(student_names)
print(student_names[3])
print(student_names[4])
student_names[4] = "rohan"
print(student_names[4])

student_names = ["ram","raj","sita","gita","rohit",78,90.6,True,78]
print(student_names)


# Tuple ()
rnos = (5,4,7,2,3,6)
print(rnos)
print(rnos[0])

rnos = (5,4,7,2,3,6,7.77,"edyoda")
print(rnos)

#rnos[4] = 30
print(rnos)

rnos = (5,4,7,2,3,6,7.77,"edyoda",5)
print(rnos)

#SET {}

rnos = {4,5,21,6,87,100}
print(rnos)

#print(rnos[2])

rnos = {4,5,21,6,87,100,"Bharati"}
print(rnos)

rnos = {4,5,21,6,87,100,"Bharati",100}
print(rnos)

#Dict

students = {6:"Ram",90:"Raj",16:"Sita"}
print(students)
students = {6:"Ram",90:"Raj",16:"Sita","a":"byju"}
print(students)

print(students[16])
print(students["a"])

students = {"a":"Ram",90:"Raj",16:"Sita","a":"byju"}
print(students)

students = {"a":"Ram",90:"Raj",16:"Sita","b":"Ram"}
print(students)

students = {"a":"Ram",90:"Raj",16:"Sita","b":5.6}
print(students)

students[90] = "Rohan"
print(students)