student = {
    "name": "Hamza",
    "age": 21,
    "marks": 85
}
print(student["name"])
print(student["marks"])

student = {
    "maths": 30,
    "physics": 85,
    "chemistry": 92
}

for subject, marks in student.items():
    if marks>=80:
        print(subject,marks)
    elif marks<40:
        print(subject,"Failed")

marks = {
    "maths": 78,
    "physics": 85,
    "chemistry": 92,
    "english": 35
}
def avg_marks(marks):
    total=0
    count=0

    for marks in marks.values():
        total += marks
        count+= 1

    return total/count
print("Average marks are",avg_marks(marks))

def highest_subject(marks):
    highest= -1
    top_subject =""

    for subject,marks in marks.items():
        if marks>highest:
            highest=marks
            top_subject=subject
    return top_subject
print("Highest marks are in", highest_subject(marks))

def failed_subject(marks):
    failed=""
    for subject,marks in marks.items():
        if marks<40:
            failed=subject
    return failed
print("Failed in", failed_subject(marks))

def result(marks):
    for mark in marks.values():
        if mark<40:
            return "Fail"
    return "Pass"

student = {
    "name": "Hamza",
    "marks": {
        "maths": 54,
        "physics": 76,
        "chemistry": 82,
        "english": 37
    }
}
print(student["name"])
print("Average marks are:", avg_marks(student["marks"]))
print("Highest marks are in", highest_subject(student["marks"]))
print("Result:", result(student["marks"]))