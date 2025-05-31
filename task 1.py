set = {"Shivam": 12, "Akshay": 89, "Alice": 85}
a = input("Enter the student's name : ")
if a in set:
    print(a+"'s marks: ", set[a])
else:
    print("Student not found.")
