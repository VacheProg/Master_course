a = open("a.txt", "rt")
b = open("a.txt", "at")
for i in range(10):
    b.write(str(i))
for i in a:
    print(i)

b.close()
a.close()
#


with open('a.txt', "rt") as f:
    for i in f:
        print(i)



