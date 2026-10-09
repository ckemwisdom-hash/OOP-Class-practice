students = ["Kem", "Boyce", "Jude"]
print(students)

print("my best friend is(student[0])")
print("my best friend is(student[1])")
print("my best friend is(student[2])")


# Get the index of an item in a list
print(students.index("Kem"))
print(students.index("Boyce"))
print(students.index("Jude"))


# Know the number of an items in a list
print(f"The total items in the list is:(len(students))")


# Add items to a list
students.append("Kem")
print("students")
students += ["Kem", "Boyce", "Jude"]


print("students")
students.insert(4, "Donald")
print(students)


# Extending a list
fruits = ["Apple", "Banana", "Mango"]
students.extend(fruits)
print(students)

# Removing an item from the list
fruits.remove("Mango")

students.pop()
students.pop()
thirdItem = students.pop()
print(students)
print(thirdItem)


  