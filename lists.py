my_numbers = [1, 4, 6, 8, 19, 20, "hey", True, 12389.123]
my_second_numbers = [123, 15, 78, 90]
print(my_numbers)
my_numbers.append(120)
print(my_numbers)
print(my_numbers.pop())
print(my_numbers)
print(my_numbers.extend("hello   "))
#1) chi ashxati qani vor list chi
#2) kavelacni hello bary
print(my_numbers)
my_numbers_copy = my_numbers
print(my_numbers_copy)
my_numbers_copy.append(123123)
print(my_numbers)
print(my_numbers_copy)

name1 = 'asdads'
name2 = name1
ankap = [1,4, 7, 2, 3, 10, 5]

print(ankap.sort(reverse=False))
print(ankap)

ankap.insert(4,123)

hey = ankap[:100]
print(ankap[::])
print(ankap.append(123))
print(hey)
print(ankap)
