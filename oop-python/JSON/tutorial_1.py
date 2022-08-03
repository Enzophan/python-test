import json

person = {
    "name": "John",
    "age": 30,
    "city": "New York",
    "hasChildren": False,
    "titles": ["engineer", "programer"],
}

# personJson = json.dumps(person, indent=4, separators=('; '))
personJson = json.dumps(person, indent=4, sort_keys=True)
print(personJson)

# Write file
with open("JSON/person.json", "w") as file:
    json.dump(person, file, indent=4)

person = json.loads(personJson)
print(person)

# Read file
with open("JSON/person.json", "r") as file:
    readJson = json.load(file)
    print(readJson)
