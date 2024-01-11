# Create an empty dictionary . Allow 4 friendsto enter their favourite langauages as values and use keys as their names. Assume that the names are unique.

from re import A


favLang = {}
a = input("Enter your favorite language Shubham\n")
b = input("Enter your favorite language Kirti\n")
c = input("Enter your favorite language Sanjay\n")
d = input("Enter your favorite language Sonali\n")
favLang['Shubham'] = a
favLang['Kirti'] =  b
# If names of 2 friends are same what will happen in this program
favLang['Shubham'] = c
favLang['Sonali'] = d


print(favLang)

# If languages of two frienda are same what will happen in this program.



