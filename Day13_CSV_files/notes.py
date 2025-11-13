# What .get() does
#     .get() is a safe way to access a value in a dictionary.

#     Normally, if you write row["name"] and the key "name" doesn’t exist,
#     → Python raises a KeyError and crashes.

#     But if you write row.get("name", "Unknown"), it does this:

#         Looks for "name" in the dictionary row

#         If found → returns its value

#         If not found → returns "Unknown" (the default value you provided)

# So .get(key, default) means:

# “Give me the value for key, but if it’s missing, use default instead.”



#example
person = {"name": "Collan", "age" : 21}

print(person["name"])#normal circumstance it will print name
print(person["temp"])#throws an error

print(person.get("temp"))#will not throw error instead it returns None
print(person.get("temp", "Temp not available" ))#returns temp not available