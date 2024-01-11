# Python Lists are container to store a set of values of any data type.(orderd)
# create a list using[]

a = [1,2,4,67,98]  #Collection of numbers
# Print the list using print() funvtion
print(a)

# access using index a[0],a[1],a[2]
print(a[2])

# Change the value of list using
a[0] = 45
print(a)
                                       # In order to slice a string we use the following syntax
                                    
print(a[3])
print(a[4])

print(a[-1])
print(a[-2])
print(a[-3])
print(a[-4])
print(a[-5])

# We can create a list with items of different types
c = [45, "Harry" , False, 67.80]
print(c)



# List Slicing
friends = ["Harry", "Tom","Rohan","Sam","Divya",45]
print(friends[0:4])                     #Slicing
print(friends[:4])  
print(friends[-4:])  
print(friends[2:4])  

a = [1,2,3]
b = [4,5,6]
c = a+b
print(len(c))



fname = raw_input("Enter file name: ")
fh = open(fname)
lst = list()                       # list for the desired output
for line in fh:                    # to read every line of file romeo.txt
    word= line.rstrip().split()    # to eliminate the unwanted blanks and turn the line into a list of words
    for element in word:           # check every element in word    
        if element in lst:         # if element is repeated
            continue               # do nothing
        else :                     # else if element is not in the list
            lst.append(element)    # append     
lst.sort()                         # sort the list (de-indent indicates that you sort when the loop ends)
print.lst()                        # print the list
