#Dictionary = Dictionary is a collection of key value pairs
#It is mutable,unodered,indexed
#Cannot contain duplicate keys


myDict ={
    "Fast": "In a Quick Manner",        #a["key"]= print "value"  , a["list"] = print[3,4,6,7]
    "Harry": "A Coder" ,
    "Marks": [1,2,5,6] ,
    "anotherdict": {'harry':'Player'}

}
print(myDict['Fast'])
print(myDict['Harry'])
myDict['Marks'] = [89,76]
print(myDict['Marks'])
print(myDict['anotherdict'])