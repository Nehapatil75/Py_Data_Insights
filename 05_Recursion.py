#Recursio   
# Recursion is a function which calls itself .It is used to directly use a mathematical formula as a function .#
#For example:-
#factorial(n)= n*factorial(n-1)

# Calculate the factorial of number
#n! = 1*2*3*4*....*n
#n! = [1*2*3*4*....n-1]*n
# n! = n*(n-1)!
#n = 4
#product = 1
#for i in range(n)
    #product= product*(i+1)
#print(product)

def factorial_iter(n):
    product = 1
    for i in range(n):
        product = product*(i+1)
    return(product)

def factorial_recursive(n):
    if n ==1 or n==0:
        return 1
    return n * factorial_recursive(n-1)

#f = factorial_iter(5)
f = factorial_recursive(7)
print(f)
  
# How this formula works.
#n * factorial_recursive(n-1)
#factorial(4)                 #function called
#4*factorial(3)
#4*[3*factorial(2)]
#4*3*[2*factorial(1)]
#4*3*2*[3][function returned]
