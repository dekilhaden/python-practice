i = 1
while i <6:
    print (i)
    i +=1

i = 1
while i <6:
    i +=1
    print (i)

i = 1
while i <6:
    print(i)
    if i ==3:
        continue
    i +=1

# defining list of strings 
list1 = ["geeksforgeeks", "C++", "Java", "Python", "C", "MachineLearning"] 
# initialises a variable 
i = 0
print("Printing list items\ using while loop") 
size = len(list1) 
# Implement while loop to print list items 
while(i < size): print(list1[i])              
i = i+1
i = 0
print("Printing list items\ using do while loop") 
