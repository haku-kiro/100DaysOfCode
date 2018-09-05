# Regular expressions

# Regular expressions are used to match patterns. If you ever need help - go to python shell, import re and run help(re) to get a list of patterns and kws

# in python a typical re is written as:

import re

pat = "\d+"
stringToSearch = "contains 42  a number 8 42"
match = re.search(pat, stringToSearch) # only returns one ?
print(match)


# you should follow your searches with an if statement to check for results

strtest = "an example word:cat!!!"
match = re.search(r"word:\w\w\w", strtest) # should make sure to use raw strings when using re
if match:
    print("found", match.group())
else:
    print("Not found")


str = 'purple alice-b@google.com monkey dishwasher'
match = re.search(r'\w+@\w+', str)
if match:
    print(match.group())  ## 'b@google'

match = re.search(r'[\w.-]+@[\w.-]+', str)
if match:
    print(match.group())  ## 'alice-b@google.com'

str = 'purple alice-b@google.com monkey dishwasher'
match = re.search(r'([\w.-]+)@([\w.-]+)', str)
if match:
    print(match.group())   ## 'alice-b@google.com' (the whole match)
    print(match.group(1))  ## 'alice-b' (the username, group 1)
    print(match.group(2))  ## 'google.com' (the host, group 2)

## Suppose we have a text with many email addresses
str = 'purple alice@google.com, blah monkey bob@abc.com blah dishwasher'
## Here re.findall() returns a list of all the found email strings
emails = re.findall(r'[\w\.-]+@[\w\.-]+', str) ## ['alice@google.com', 'bob@abc.com']
for email in emails:
# do something with each found email string
    print(email)


# findall in a file:
path = r"C:\Users\mdjco\Desktop\100DaysOfCode\Day30\test.txt"
emailPattern = r'[\w\.-]+@[\w\.-]+'
with open(path, 'rb') as f:
    emails = re.findall(emailPattern, f.read().decode()) # note, had to read as byte (rb flag, and then decode the data to actually read the file)
    count = 0
    for email in emails:
        print(email)
        count += 1
    print(f"Found this many emails: {count}")
    print(emails) # this would be the list of matches


# re.sub(pat, replacement, str) syntax
str = 'purple alice@google.com, blah monkey bob@abc.com blah dishwasher'
## re.sub(pat, replacement, str) -- returns new string with all replacements,
## \1 is group(1), \2 group(2) in the replacement
print(re.sub(r'([\w\.-]+)@([\w\.-]+)', r'\1@yo-yo-dyne.com', str))
## purple alice@yo-yo-dyne.com, blah monkey bob@yo-yo-dyne.com blah dishwasher
