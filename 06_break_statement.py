# Break Statement
#break is used to comes out of the loop whwn encountered .It insreucts the program to - exit the loop now

for i in range(10):
    print(i)
    if i==5:
        break
  
#else:
#  print("This is inside else of for")

for i in range(10):
    if i==5:
        continue
    print(i)
