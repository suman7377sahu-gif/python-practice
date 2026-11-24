# 2. Write a program to find out whether a student has passed or failed if it requires a total of
# 40% and at least 33% in each subject to pass. Assume 3 subjects and take marks as an
# input from the user.
Total_marks = 300  # Assuming each subject is out of 100 marks

marks1 = int(input("Enter marks obtained in subject 1: "))
marks2 = int(input("Enter marks obtained in subject 2: "))
marks3 = int(input("Enter marks obtained in subject 3: ")) 

total_obtained = marks1 + marks2 + marks3

if (total_obtained >= (0.4 * Total_marks)) and (marks1 >= 33) and (marks2 >= 33) and (marks3 >= 33):
    print("The student has passed.")
else:
    print("The student has failed.")
