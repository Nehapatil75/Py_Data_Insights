#Write a program to accept marks of 6 students and display them ina= a sorted manner.
m1 = int(input("Enter   Marks for Student  Number 1: "))
m2 = int(input("Enter   Marks for Student  Number 2: "))
m3 = int(input("Enter   Marks for Student  Number 3: "))
m4 = int(input("Enter   Marks for Student  Number 4: "))
m5 = int(input("Enter   Marks for Student  Number 5: "))
m6 = int(input("Enter   Marks for Student  Number 6: "))

myList = [m1,m2,m3,m4,m5,m6]
myList.sort()
print(myList)