
def a():
    pass

def my_function(required_argument, default_argument=3, def_arg_1=20,  *args, **kwargs):
    print(required_argument)
    print(default_argument)
    print(def_arg_1)
    print(args)
    print(kwargs)


# my_function(10, default_argument=104, def_arg_1=89, 10, 20, 40, hello='hi')



def hey(a = 10, b=25, *args):
    pass


hey(10, 64, 10)



def set_vars(a, b, c, d, k=10, k1=15):
    print(a)
    print(b)
    print(c)
    print(d)
    print(k)
    print(k1)

my_vars = (10, 15, 20, 25)
my_vars2 = {'k': 'v', 'k1': 'v1'}
set_vars(*my_vars, **my_vars2)


def simple_lambda(x):
    return x[1]

f = lambda x:x[1]

print(sorted([(1, 5, 10), (4, 20, 2), (10, 1, 15)], key=lambda x: x[1]))
a = (1, 5, 10)
b = (4, 20, 2)
print(f(a) < f(b))

print(f(a))

print([0]*100)



def f(a = None):
    if a is None:
        a = []
    a.append(15)
    print(a)

f()
f(a=['hello'])
f(a=['hello'])
f()


def my_func(a:int, b:str):
    pass

