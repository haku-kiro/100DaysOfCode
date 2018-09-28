# Day 54

## Objectives

Working on datacamp.com

## Resources

- <http://datacamp.com>

### Setup

- webz

### Suggested plan for tomorrow

- Should really go through this content at some point...
- Writing xml files
  - <https://csharp.net-tutorials.com/xml/writing-xml-with-the-xmlwriter-class/>
- Do some more stuff with wcf
  - composite types to service operations
- Cover a few design patterns: Like the proxy pattern (This might not relate, <https://docs.microsoft.com/en-us/dotnet/framework/wcf/how-to-create-a-wcf-client> but check it out (The proxy section that is (Svcutil.exe section)))
- Read up on how to use the Svcutil.exe tool (To create the source and config file)
- wcf service configuration editor (Look at how this tool functions as well. Under tools vs)
- Cover the 'See Also' section under: <https://docs.microsoft.com/en-us/dotnet/framework/wcf/how-to-use-a-wcf-client>
- Do some work with async and await, or some threading - parallel tasks etc
- Cover how IL works, and the implications of compiler theory
- Need to look into how to make a method `Awaitable`
- Still need to finish the edx course on computing with python.

### Random Notes

- Learn the diff between correlation cofficient and covariance.
- Code to check built in methods, things and stuffs

```python
import builtins

dir(builtins)
```

- You can have inner functions in python:

```Python

# Define three_shouts
def three_shouts(word1, word2, word3):
    """Returns a tuple of strings
    concatenated with '!!!'."""

    # Define inner
    def inner(word):                                                 # <---- woah
        """Returns a string concatenated with '!!!'."""
        return word + '!!!'

    # Return a tuple of strings
    return (inner(word1), inner(word2), inner(word3))

# Call three_shouts() and print
print(three_shouts('a', 'b', 'c'))

```