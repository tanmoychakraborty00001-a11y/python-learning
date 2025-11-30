# Ex06_03 – Traversing List
marks = [62, 70, 80, 65, 92, 55]
print("All marks")

for i in marks:
    print(i)

print("marks > 50: ")
for i in marks:
    if i > 50:
        print(i)

print("Maximum marks: ", max(marks))
print("Maximum marks: ", min(marks))