#!/usr/bin/python
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

import sys
import re
import os
import shutil
import subprocess

"""Copy Special exercise
"""


# +++your code here+++
# Write functions and modify main() to call them
def get_special_paths(path):
  """
  Return the absolute paths of the dir that is passed in
  """
  try:
    filenames = os.listdir(path)
    for file in filenames:
      print(os.path.abspath(file))
  except:
    # silent fail - just takes out complexity of checks
    #print("There was an error")
    pass


def copy_to(paths, dir):
  """
  Copies to the dir specificed
  """
  # dir would be the place to copy to
  # paths would be the things being copied to dir

  print("Running the copy command")

  # Check dir exists:
  if not os.path.exists(dir):
    os.makedirs(dir) # have to use mkdirs to make sure that each dir is created on chain
  
  # for each path, copy to dir
  try:
    for path in paths:
      shutil.copy(path, dir)
  except:
    print(f"An error occured when copying files to: {dir}")
    print("Check the path of the files you are copying")
    return
  print("Your file has copied")

# using powershell 'Compress-archive'
def zip_to(paths, zippath):
  # btw, if you want to create a ps array - as a param, for example, just seperate the values by a comma
  zipFiles = ''
  for path in paths:
    zipFiles += path + ', '
  _zipFiles = zipFiles[:-2]

  # may take long as this is the 'best' compression 
  (status, output) = subprocess.getstatusoutput(f"powershell Compress-Archive -path {_zipFiles} -destinationpath {zippath} -compressionlevel Optimal") 
  if status > 0:
    print("Failed to compress the file, sorey about that...")
    print(output)
  else:
    print("Compression has occured...")


def main():
  # This basic command line argument parsing code is provided.
  # Add code to call your functions below.

  # Make a list of command line arguments, omitting the [0] element
  # which is the script itself.
  args = sys.argv[1:]
  if not args:
    print("usage: [--todir dir][--tozip zipfile] [dir ...]")
    sys.exit(1)

  # todir and tozip are either set from command line
  # or left as the empty string.
  # The args array is left just containing the dirs.
  todir = ''
  if args[0] == '--todir':
    todir = args[1] # gets the destination
    del args[0:2]
    copy_to(args, todir)

  tozip = ''
  if args[0] == '--tozip':
    tozip = args[1]
    del args[0:2]
    zip_to(args, tozip)

  # list of absolute paths:
  if len(args) >= 1:
    for arg in args:
      get_special_paths(arg) # arg should be a directory/file

  if len(args) == 0:
    print("error: must specify one or more dirs")
    sys.exit(1)

  # +++your code here+++
  # Call your functions
  
if __name__ == "__main__":
  main()
