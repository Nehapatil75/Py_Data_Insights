# Write a program to calculate the factorial of a given number using for loop.

#n! = 1 X 2 X 3 X 4 X 5 X 6........X n
# 5! = 1 X 2 X 3 X 4 X 5

num = int(input("Enter the number :"))
fact = 1
for i in range(1, num+1):
    fact = fact*i

print(f"The fact of this number is {fact}")