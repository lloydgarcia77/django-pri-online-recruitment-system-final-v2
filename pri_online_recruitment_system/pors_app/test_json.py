import json

# You can parse a JSON string using json.loads() method. The method returns a dictionary.

person = '{"name": "Bob", "languages": ["English", "Fench"]}'
person_dict = json.loads(person)

print(person)

print(person_dict['languages'])

# You can use json.load() method to read a file containing JSON object.
# Here, we have used the open() function to read the json file. Then, the file is parsed using json.load() method which gives us a dictionary named data.

with open('../person.json') as f:
    data = json.load(f)

print(data)

# You can convert a dictionary to JSON string using json.dumps() method


"""
+--------------+----------------------+
|    Python    |   JSON Equivalent    |
+--------------+----------------------+
|  dict        |       object         |
|  list, tuple |       array          |
|  str         |       string         |
|  int         |   float, int number  |
|  True        |       true           |
|  False       |       false          |
|  None        |       null           |
+--------------+----------------------+
 
"""
#To write JSON to a file in Python, we can use json.dump() method.
#In the above program, we have opened a file named person.txt in writing mode using 'w'. If the file doesn't already exist, it will be created. Then, json.dump() transforms person_dict to a JSON string which will be saved in the person.txt file.

person_dict = {"name": "Bob",
"languages": ["English", "Fench"],
"married": True,
"age": 32
}

with open('../person.txt', 'w') as json_file:
    json.dump(person_dict, json_file)


#To analyze and debug JSON data, we may need to print it in a more readable format. This can be done by passing additional parameters indent and sort_keys to json.dumps() and json.dump() method.

person_string = '{"name": "Bob", "languages": "English", "numbers": [2, 1.6, null]}'

# Getting dictionary
person_dict = json.loads(person_string)

# Pretty Printing JSON string back
print(json.dumps(person_dict, indent = 4, sort_keys=True))