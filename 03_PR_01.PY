# Write a program to create a dictionary of hindi words with value as thier english translation.provide user with an option to lookit up!

myDict = {
    "Pankha": "Fan",
    "Dabba":" Box",
    "Vastu":"Item"
}
print("Options are ",myDict.keys())
a = input("Enter the Hindi Word\n")
#print("The meaning of your wprd is:",myDict[a])

#Below list will not throw an error if the key is not present in the dictionary
print("The meaning of your wprd is:",myDict.get(a))
