# Standard utilities module
import os
import shutil

# can list the files in a dir
filenames = os.listdir("./")
print(filenames) # returns a list of the specified directory
# The above only returns the filenames, not the absolute path

# to add the full path, use the following:
for file in filenames:
    fullPath = os.path.join(os.getcwd(), file)
    print(fullPath)

# giving a path return an absolute path:
print(os.path.abspath("./file1.py")) # which makes me think...

for file in filenames:
    print(os.path.abspath("./" + file)) # can return the absolute path like this as well

# to return the base directory for a file:
print(os.path.dirname("./file1.py")) # would be more useful if you want to extract it from the string (in which case, just use re)

# you can check to see if a directory/file exits
print(os.path.exists("./")) # the curr directory will always exist

# if the dir exists, wont create again, will throw an error

# you can make a dir with:
#os.mkdir("./TestDir")

# if you want to create a chain of directories, you can use this instead (creates all the directorys specified)
#os.makedirs("./ThisOne/andThisOne");

# You can copy files with:

#shutil.copy("source", "dest")
#shutil.copy("./file1.py", "./file2.py") can't rename files like this

# Todo, find out how to rename a file


# Running an external processes
# used to be done in the commands module, python 3 uses subprocess
import subprocess

# run a command, wait for it to exit and return it's status int and output text as a tuple
# the status is usually non-zero if it failed
# the error and the 
(status, output) = subprocess.getstatusoutput(r"dir | findstr -ir \day")
print(status)
print(output)

# This is really cool

# you can do the above, but not return the status code:
output = subprocess.getoutput("tree /F") # I wonder: woah... Sick
print(output)

# TODO readup on popen2 - which i think is deprecated, now mostly covered in subprocess?

# if you just want to run a command, ie, you don't want to capture the output >
os.system("dir")

# Catching exceptions:

# You can add the try/except block to handle exceptions:
# Like c# you can catch certain exceptions first/over other exceptions - as a general rule, go from most specific to least
try:
    with open("This doesn't exist") as f:
        print(f.read())
except IOError:
    print("An IOError has occured")
except:
    print("Something went wrong, I guess..")


# urllib.request module provides url fetching, the urlparse module provides url manipulation
import urllib.request

# to fetch a file like object from a website:
urlFile = urllib.request.urlopen(r"https://developers.google.com/edu/python/utilities")
# urlFile = urllib.request.urlopen(r"https://reddit.com")
urlFile = urllib.request.urlopen(r"https://www.google.com") # adding this bec got too many requests error from reddit

# commenting out bec of the amount of output
# This would be each line of the source for the page that you request
# for line in urlFile:
#     print(line)

# you can also read the urlFile like a generic file:
data = urlFile.read() # note, the methods are not showing up on intellisense - they are there though

# you can get the meta info for that request:
info = urlFile.info()
print(info)

# you can get the base url for the urlFile (Which might differ bec of redirects)
baseUrl = urlFile.geturl() # This throws a too many requests error, on reddit
print(baseUrl)


# you can download a websites content: (Just overwrites the data - if you make the request again)
urllib.request.urlretrieve(r"http://www.google.com", "testUrlData.txt")

