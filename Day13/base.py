import os 

# Getting input from a user:
print(os.getpid())


# Comment out bec of vs code things...
theInput = input("Enter some text\n")
print(theInput)



# Open/create a file 

# this mode is for reading and writing, overwrites the file as well
with open("testFile.txt", "w+") as file: # the second arg is the method mode you open the file for 
    file.write("This is some random text")
    # you don't have to use the file.close() method when using the 'with' construct
    # the file modes are: https://www.tutorialspoint.com/python/python_files_io.htm
    print(file.read()) # read the contents of the file

with open("testFile.txt", "r+") as file:
    value = file.read(3) # reads only 3 chars from the file
    print(value)
    pos = file.tell() # returns the current position of the file object
    print(pos) # would be 3 after reading until that point
    # to reset the position:
    file.seek(0,0)
    pos = file.tell()
    print(pos) # reset the pos


# renaming a file
# arg1: file name, arg2: new file name
os.rename("testFile.txt", "testFile.md")

# removing a file (Note: if the file doesn't exist throws an error)
os.remove("testFile.md")

# making a dir
os.mkdir("./testDir")

# removing a dir
os.removedirs("./testDir")

# Changing to a dir (throws an error if the dir doesnt exist)
# os.chdir("./testDir") # commenting out bec the dir shouldn't exist - just got deleted

# return the current dir
print(os.getcwd()) # returns the absolute path not the relative

# return the current user login that is running the current process
print(os.getlogin()) # note some diff for unix based systems - this would be os.geteuid()

# return the current process id
print(os.getpid()) # can be used to kill a process amongst other things

