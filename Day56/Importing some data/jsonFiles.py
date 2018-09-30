# how to pull data from apis and json

import json

# Load JSON: json_data
with open("a_movie.json") as json_file: # Don't have a copy of this file
    json_data = json.load(json_file)


print(type(json_data)) # prints dict

# Print each key-value pair in json_data
for k in json_data.keys():
    print(k + ': ', json_data[k])
