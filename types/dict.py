

my_dictionary = {"key": "value", 10 : 20, 15: [1,2,3]}

my_dictionary
print(my_dictionary.update({'hello':"world"}))
print(my_dictionary.keys())
print(my_dictionary.values())
print(my_dictionary.items())
print(my_dictionary.get("key", 10))
print(my_dictionary.setdefault('key2', 10))
print(my_dictionary.setdefault('key2', 125))

my_dictionary['key3'] = [13, 16, 90]

print(my_dictionary.setdefault("key3", []).append(10))
print(my_dictionary.setdefault("key3", []).append(10))
print(my_dictionary.setdefault("key3", []).append(10))
print(my_dictionary)