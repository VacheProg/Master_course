my_set = {"Hakob", "Hayk", 'Arman', 'Tiko'}
my_set1 = {"Hakob", "Hrant", 'Ani'}

my_set.add("David")
print(my_set)

print(my_set)
my_set.update(["Vache", 'asdjnasd', 'ajdas', 'Hakob'])
print(my_set.union(my_set1))
print(my_set.intersection(my_set1))
print(my_set.difference(my_set1))
print(my_set.intersection_update(my_set1))
my_set = my_set.intersection(my_set1)
print(my_set.isdisjoint(my_set1))
# print(my_set.symmetric_difference())

new_set = my_set | my_set1
new_set = my_set & my_set1
new_set = my_set ^ my_set1
new_set = my_set - my_set1
print(new_set)