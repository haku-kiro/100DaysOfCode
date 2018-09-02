# just some basic string stuff:

stringVar = "This is a string"
print(stringVar[1]) # can use the [] notation to access elements of a string, if that element doesn't exist. Throws error
print(len(stringVar)) # Can return the length of a string. This and [] can be used on most sequence types
print("String 1" + stringVar) # can concat strings with '+'

# unlike other programming languages, the print doesn't parse the values to string - you have to do that
print("THis and " + str(123))


# Side note, number wise
# To increment, you can't use ++, you have to use += or -= to decrement
# if you want to perform integer division, you should use:
print(str(12.3//4)) ## double slashes

# the raw string literal doesn't parse special chars or escape chars:
print("THis is \n Not \n a raw string")
print(r"THis is \n a raw string")

# string methods
baseVar = "This is a test Variable    "
# strings are objects, the following would be methods implemented on the string object (Like oop, c# class objects that have methods on them. or value type extension methods)

# upper and lower
# To convert a string to upper case or lower case
print(baseVar.lower()) # all lower case
print(baseVar.upper()) # All upper case

# strip
print(baseVar.strip()) # removes all whitspace from the front and end

# isalpha/ isdigit/ isspace
print(baseVar.isalpha()) # tests to see if alpha type
print(baseVar.isdigit()) # tests to see if digit type
print(baseVar.isspace()) # tests to see if whitespace

# startswith / endswith
print(baseVar.startswith("This")) # checks to see if string starts with the value
print(baseVar.endswith("Variable")) # Checks to see if the string ends with the value

# find
print(baseVar.find("test")) # looks for the parm in the string, not RE like, returns the first instance -1 if it doesn't exist

# replace
print(baseVar.replace("a", "an")) # finds all the appearances of the first param and replaces it to the second param

# split 
print(baseVar.split(" ")) # returns a list of substrings seperated by the given delimeter
# Note, if no param is passed - splits by whitespace

# join
print("-".join(baseVar.split())) # joins all the values in the list (param passed) by the delimeter (string method is used on)

## There are a lot more string methods - if you ever need any, check the python string documentation/ or docs in general



# String slice syntax

test = "Hello"
print(test[-5]) # returns H # This is where len may com in useful
print(test[-4]) # returns e
print(test[-3]) # returns l
print(test[-2]) # returns l
print(test[-1]) # returns o

print(test[-5:]) # just returns the whole string
# you can substring something
print(test[1:3]) # from index, to position (KEEP THIS IN MIND)


# unicode strings:
# regular strings in python are not unicode, they are just bytes, to create a unicode string - prefix it with 'u'
# testUnicode = u"This is unicode \u018e string \xf1" # read up on this
# print(testUnicode) # commenting out bec the \u018e string doesn't map to anything?

# to convert a unicode string to a byte encoding such as utf-8, use the following:
print(u"\xf1".encode("utf-8")) # not too sure what is happening with encoding and decoding strings to bytes/unicode etc

# python if statements:
# there is no braces, the indentation and a colon does what braces do in other languages
if True:
    print("Will always run")

# conditional statements are spelt out, not || && !=
if True or False:
    print("Will also, always run")

# the else statement exists, but if you want to chain else if statements you have to use elif
if False:
    print("Wont ever run")
elif True:
    print("Will always run")
else:
    print("Wont run...")


# TODO: do the basic exercise, string1.py                 
