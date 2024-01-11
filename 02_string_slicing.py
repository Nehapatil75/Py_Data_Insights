greeting = "Good Morning"
#name = "Harry"
#print(type(name))
#print(greeting + name)    # Add two strings
# Concatenating two string
#c = greeting + name
#print(c)

name = "Harry"
print(name[0])
print(name[1])
print(name[2])
print(name[3])
print(name[4])

print(name[-1])
print(name[-2])
print(name[-3])
print(name[-4])
print(name[-5])
#name[3] = "d"  -->Does  not work

print(name[0:3])

print(name[1:4])

print(name[-1:4])

print(name[:3])  # is same as name[0:3]

print(name[3:])   # is same as name [3:4] blank space consist length of string
print(name[-4:-1])



# slicing with skip value
name = "Harry is good"
d = name[1:4:1]
print(d)
print(name[0::2])
