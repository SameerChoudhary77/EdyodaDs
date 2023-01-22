# Girl's college

# gender = input("Enter your gender(enter F for female and M for male):" )
# cut_off = 60
# if gender == "F":
#     qualification = int(input("Enter your qualification (Enter 10 for 10th)"))
#     if qualification == 10:
#         percentage = float(input("Enter your 10th percentage: "))
#         if percentage >= 60:
#             print("Congratulations! You are eligible! ")
#         else:
#             print("Sorry you have not passed the cut-off")
#     else:
#         print("We only provide jr.college admission here ")
# else:
#     print("This is girl's college, hence only girls are allowed")





name = input("Enter your name: ")
roll_no = int(input("Enter your roll number: "))
maths_marks = int(input("Enter your Maths marks out of 100 "))
english_marks = int(input("Enter your English marks out of 100 "))
science_marks = int(input("Ënter your Science Marks out of 100 :"))

total = maths_marks + english_marks + science_marks
fix_total = 300
percentage = total/fix_total * 100


if percentage >= 90:
    grade = "A"
elif percentage >= 80 and percentage < 90:
    grade = "B"
elif percentage >= 70 and percentage < 80:
    grade = "C"
elif percentage >= 60 and percentage <70:
    grade = "D"
elif percentage >= 50 and percentage <60:
    grade = "E"
elif percentage >= 40 and percentage <50:
    grade = "E+"
else:
    grade = "F"

print("*****************Report Card***********************")
print("Name: ",name, "\nMaths Marks is: ",maths_marks,"\nEnglish Marks is: ",english_marks,"\nScience Marks is: ",science_marks,"\nTotal Marks is: ",total,"\nThe percentage is: ",percentage,"\nThe grade is: ",grade)


