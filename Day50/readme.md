# Day 50

## Objectives

Working on datacamp.com

## Resources

- <http://datacamp.com>

### Setup

- c# project file

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

```Python
# just something to look into, this is kind of the power of numpy arrays
# height and weight are available as a regular lists

# Import numpy
import numpy as np

# Calculate the BMI: bmi
np_height_m = np.array(height) * 0.0254
np_weight_kg = np.array(weight) * 0.453592
bmi = np_weight_kg / np_height_m ** 2

# Create the light array
light = bmi < 21

# Print out light
print(light)

# Print out BMIs of all baseball players whose BMI is below 21
bmi[light]
```