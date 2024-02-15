num_students = int(input("Enter number of students : "))
details = {}
for i in range(num_students):
    name = input("Enter student Name:")
    score = int(input("Enter student Score"))
    details[name] = score
print("Student Name","Student Score")
for items in details.items():
    print(items[0],items[1])