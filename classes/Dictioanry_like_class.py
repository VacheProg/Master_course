import uuid
#
#
# class MyDict:
#     def __init__(self):
#         self._data = {}
#
#     def __getitem__(self, key):
#         print(f"Getting key: {key}")
#         return self._data[key]
#
#     def __setitem__(self, key, value):
#         print(f"Setting {key} = {value}")
#         self._data[key] = value
#
#     def __delitem__(self, key):
#         print(f"Deleting key: {key}")
#         del self._data[key]
#
#     def __contains__(self, key):
#         return key in self._data
#
#     def __len__(self):
#         return len(self._data)
#
#     def __iter__(self):
#         return iter(self._data)   # iterate keys
#
#     def __repr__(self):
#         return f"MyDict({self._data})"
#
#
#
# # Usage example
#
# new_dict = {'a':'b'}
#
# new_dict['new_key'] = "hey"
# new_dict.__setitem__("new_key", "hey")
# print(new_dict["a"])
# print(new_dict.__getitem__("a"))
#
#
# d = MyDict()
# d["name"] = "Alice"
# print(d["name"])# neutral example
# # print(d.__getitem__("name"))# neutral example
# print(d)
#
# print(d)
#
#
# d["age"] = 30
#
# print(d["name"])
# print("name" in d)
#
# del d["age"]
# print(len(d))
#
# for k in d:
#     print(k, d[k])
#
# print(d)
#
#
#



class Cell:
    def __init__(self, name, x, y):
        self.id = uuid.uuid4()
        self.name = name
        self.x = x
        self.y = y

    def __eq__(self, other):
        if not isinstance(other, Cell):
            return NotImplemented
        return (self.name, self.x, self.y) == (other.name, other.x, other.y)

    def __hash__(self):
        return f"Cell({self.name})"
        # return self.id

    def __repr__(self):
        return f"Cell({self.name}, {self.x}, {self.y})"




c1 = Cell("A1", 10, 20)


print(c1.id)
# c2 = Cell("A1", 10, 20)
# c3 = Cell("B2", 5, 8)
#
#
# new_dictionary = {c1:10}
#
# print(c1 == c2)
# Use inside a set
# s = {c1, c2, c3}
# print(s)
#
# # Use as dictionary keys
# d = {c1: "Placed", c3: "Unplaced"}
# print(d[c1])
