# Default Parameter
# We can have a value as default argument in a function.If we specify name= 'stranger'in the line containary def,this value is used when no argument is passed.

def greet(name='Stranger'):    
    print("Good day"+name)      # Function definition


greet("Harry")       #Name will be "Harry" in function body(passed)
greet()              #Name will be "Stranger" in function body(passed)
