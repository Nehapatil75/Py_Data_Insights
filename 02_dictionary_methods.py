myDict ={
    "Fast": "In a Quick Manner",        
    "Harry": "A Coder" ,
    "Marks": [1,2,5,6] ,
    "anotherdict": {'harry':'Player'}

}

#Dictionary Methods
print(myDict.keys())       # Prints the keys of the dictionary
print(list(myDict.keys()))  # Prints the keys of the dictionary
print(myDict.values())      #Prints the (key,value) for all contains of  the dictionary
print(myDict)
updateDict = {
    "Lovish":"Friend",
    "Shubham":"Freind",
    "Divya": "Freind",
    "Harry": "Dancer"
}
myDict.update(updateDict)  #Updates the dictionary by adding key-values pairs from updateDict
print(myDict)

print(myDict.get("Harry")) # Prints value associated with key "Harry"
print(myDict["Harry"])     #Prints value associated with key "Harry"

#The Diffference between.get and []syntax in Dictionary
print(myDict.get("Harry2")) # Returns None as Harry2 is not present in the dictionary
print(myDict["Harry2"])     #throws an error as Harry is not present in the dictionary
