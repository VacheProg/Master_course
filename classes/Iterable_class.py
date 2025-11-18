
l = [1,2,3,54,6]


class  MyList:
    def __init__(self, *args):
        self.values = list(args)
        self.idx = -1



    def append(self, obj):
        self.values.append(obj)

    def extend(self):
        pass

    def sum(self):
        pass

    def max(self):
        pass

    def min(self):
        pass

    def __iter__(self):
        for i in self.values:
            yield i

    def __next__(self):
        self.idx += 1
        if self.idx >= len(self.values):
            raise StopIteration()
        return self.values[self.idx]

l = [1, 3, 5, 56]


# print('\n'.join(dir(l)))
my_l = MyList(1, 3, 5, 56)


# print(next(my_l))
# print(next(my_l))
# print(next(my_l))
# print(next(my_l))
# print(next(my_l))
#
#
for i in my_l:
    print(i)



for i in my_l:
    print(i)


