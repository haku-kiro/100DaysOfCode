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

- Look at practising the 'Python Data Science Toolbox (part 1)' course some more
- When you use map, make sure to convert to a list when done

```Python

# Create a list of strings: spells
spells = ["protego", "accio", "expecto patronum", "legilimens"]

# Use map() to apply a lambda function over spells: shout_spells
shout_spells = map(lambda x: x + '!!!', spells)

# Convert shout_spells to a list: shout_spells_list
shout_spells_list = list(shout_spells)

# Convert shout_spells into a list and print it
print(shout_spells_list)


```

- Applying a filter to a list (sort of like pandas isin method)

```Python

# Create a list of strings: fellowship
fellowship = ['frodo', 'samwise', 'merry', 'pippin', 'aragorn', 'boromir', 'legolas', 'gimli', 'gandalf']

# Use filter() to apply a lambda function over fellowship: result
result = filter(lambda x: len(x) > 6, fellowship)

# Convert result to a list: result_list
result_list = list(result)

# Convert result into a list and print it
print(result_list)


```

- While I'm at it:

```Python

# Import reduce from functools
from functools import reduce   # to use reduce you have to do this, Q: what else is in here ?

# Create a list of strings: stark
stark = ['robb', 'sansa', 'arya', 'brandon', 'rickon']

# Use reduce() to apply a lambda function over stark: result
result = reduce(lambda item1, item2: item1 + item2, stark)

# Print the result
print(result)


```

- Raising an error

```Python

# Define shout_echo
def shout_echo(word1, echo=1):
    """Concatenate echo copies of word1 and three
    exclamation marks at the end of the string."""

    # Raise an error with raise
    if echo < 0:
        raise ValueError('echo must be greater than 0')

    # Concatenate echo copies of word1 using *: echo_word
    echo_word = word1 * echo

    # Concatenate '!!!' to echo_word: shout_word
    shout_word = echo_word + '!!!'

    # Return shout_word
    return shout_word

# Call shout_echo
shout_echo("particle", echo=5)

```

- When unpacking a dict arg:

```Python

def easy_print(**a):
        for p, q in a.items():
            print('The value of ' + str(p) + " is " + str(q))
easy_print(x = 10, y = 20)

```