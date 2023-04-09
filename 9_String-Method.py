# strings are immutable 
a = "Sandy!!!!!"
print(len(a))
print(a)
print(a.upper())
print(a.lower())
print(a.rstrip("!")) #rstrip means to remove the given thing
print(a.replace("Sandy","Silicon"))
print(a.split(" "))

#capitalize
blogheading="intrOduction tO js"
print(blogheading.capitalize())

str1 = "Welcome to our website"
print(str1.center(50))

print(str1.endswith("website", 6,21))
print(str1.find("i"))
print(str1.index("e"))
print(str1.isalpha())

# we can use other functions like:
# islower()-returns true or false
# isprintable()- returns true or false 
# isspace()- tells if space is present ot not in given variable 
# istitle()- returns true only if the first letter of each word of the string is capitalized else it returns false   
# startswith()-tells true if is same with startswith(string) or else false 
# swapcase()- converts lowercase to uppercase and vice versa


