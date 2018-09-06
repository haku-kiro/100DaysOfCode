#!/usr/bin/python
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

import sys
import re

"""Baby Names exercise

Define the extract_names() function below and change main()
to call it.

For writing regex, it's nice to include a copy of the target
text for inspiration.

Here's what the html looks like in the baby.html files:
...
<h3 align="center">Popularity in 1990</h3>
....
<tr align="right"><td>1</td><td>Michael</td><td>Jessica</td>
<tr align="right"><td>2</td><td>Christopher</td><td>Ashley</td>
<tr align="right"><td>3</td><td>Matthew</td><td>Brittany</td>
...

Suggested milestones for incremental development:
 -Extract the year and print it
 -Extract the names and rank numbers and just print them
 -Get the names data into a dict and print it
 -Build the [year, 'name rank', ... ] list and print it
 -Fix main() to use the extract_names list
"""

def extract_names(filename):
  """
  Given a file name for baby.html, returns a list starting with the year string
  followed by the name-rank strings in alphabetical order.
  ['2006', 'Aaliyah 91', Aaron 57', 'Abagail 895', ' ...]
  """
  result = []

  with open(filename, 'r') as f:
    #To read the year from the filename (Not perfect, could get another 4 digit number from the path) /Should be getting the year from the file contents
    # <h3 align="center">Popularity in 1990</h3>
    yearPattern = r"<h3.*>(.*)(\d\d\d\d)</h3>" # bec I am using the greedy match in the element, I have to be explicit with the year ?
    year = re.search(yearPattern, f.read())
    if year:
      result.append(year.group(2))
    else:
      print("No year?")
      # want to break here?

    # Extract the rank, and the name
    # <tr align="right"><td>1</td><td>Michael</td><td>Jessica</td>
    rankAndNamePattern = r"<tr.*><td>(\d+)</td><td>(\w+)</td><td>(\w+)</td>"
    f.seek(0) # set this to re-read the file after each read/ room for optimization here
    data = re.findall(rankAndNamePattern, f.read())
    
    # This seems like it would be inefficient?
    boyCollection = [f"{boyname} {rank}" for rank, boyname, girlname in data] # we need to make sure that we unpack the tuple correctly, even if we only use one of the vars
    girlCollection = [f"{girlname} {rank}" for rank, boyname, girlname in data]
    dataset = boyCollection + girlCollection
    dataset.sort()

    # I want the result to be in a list, therefore I need to loop over the list
    for item in dataset:
      result.append(item)
    # instead of the following:
    #result.append(dataset)
  
  print(result)

  #Want to write the results to a file, just to make sure that it worked (Note, have to append to the file as this method could be called many times)
  with open("BabyNamesLogFile.txt", "a") as f: # 'a' creates the file if it doesn't exist as well
    for lineToWrite in result:
      f.write(str(lineToWrite)+ " ") # formatting
    f.write("\n\n")


def main():
  # This command-line parsing code is provided.
  # Make a list of command line arguments, omitting the [0] element
  # which is the script itself.
  args = sys.argv[1:]

  if not args:
    print('usage: [--summaryfile] file [file ...]')
    sys.exit(1)

  # Notice the summary flag and remove it from args if it is present.
  summary = False
  if args[0] == '--summaryfile':
    summary = True
    del args[0]
    for fileName in args:
      extract_names(fileName)
  # +++your code here+++
  # For each filename, get the names, then either print the text output
  # or write it to a summary file
  
if __name__ == '__main__':
  main()
