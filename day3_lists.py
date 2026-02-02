marks = [78, 85, 92, 67]

print(marks[0])
print(len(marks))

marks = [78, 85, 92, 67]

total = 0
for m in marks:
    total = total + m

print("Average =", total / len(marks))

marks = [78, 85, 92, 67, 88]
for i in marks:
    if i>=80:
     print(i)
count=0
for i in marks:
    if i<=70:
        count+=1
print(count)

max_value=marks[0]
for i in marks:
    if i>max_value:
        max_value=i
print(max_value)