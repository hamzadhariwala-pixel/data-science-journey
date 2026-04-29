students_marks = {"Alice":"85", "Billy":"56","Carol":"92", "Dora":"67"} #made a dictionary containing students and marks obtained.
user_input= input("Enter the student's name: ")#taking user input for name of student
if user_input in students_marks:
    print(user_input,"'s marks: ", students_marks[user_input], sep="") 
else:
    print ("Student not found.")