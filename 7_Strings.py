name = "Sandy" 
friend="Rohan"
anotherfriend= 'Lovish'
apple= '''He said, 
 \"I want to eat apple"'''
# if you want to print something in double quote like 
# in direct speech then use single code around the string

#  we can also use ''' 

print("Hello, " + name)
print(apple)

print(name[0]) 
print(name[1]) 
print(name[2]) 
print(name[3]) 
print(name[4])
# print(name[5]) Throws an error

print("\nLet's use a for loop\n")
for character in apple:
    print(character)



# NOTE- INDEX ERROR
# when an object is tried to access is not available
#or not declared