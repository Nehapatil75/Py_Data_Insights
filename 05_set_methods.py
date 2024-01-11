#Creating an empty set

b =set()
print(type(b))

#Set Methods
#Adding values to an empty set
b.add(4)
b.add(5)
b.add(5)
b.add(5) #Adding a value repeatedly does not changes a set
b.add(4)
#b.add([4,5,6])       #Cannot add list or dictionary to sets

##Accessing Elements
#b.add({4:5})         #Cannot add list or dictionary to sets
b.add((4,5,6))
print(b)

#Length of set
print(len(b)) # Prints the length of the set

#Removal of an item
#b.remove(15) # Throws an error while to remove 15(which is not present in the set)
b.remove(5)# removes 5 from set b
print(b)


#Pop method
print(b.pop())  # Removes an arbritary element from the set and returns the element removed.


#Union method 
# Returns a new set with all items from both sides

#Intersection method
#Returns a set which contains only items in both sets.