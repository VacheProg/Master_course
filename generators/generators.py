# ============================================
# Python Generators Examples
# Covers yield, yield from, generator expressions,
# control flow, and exception handling
# ============================================

# 1️⃣ Basic Generator Function



def count_up_to(n):
    """Yields numbers from 1 to n."""
    i = 1
    while i <= n:
        yield i
        i += 1

# for i in count_up_to(10):
#     print(i)
my_gen = count_up_to(100)
print(next(my_gen))
print(next(my_gen))
print(next(my_gen))
print(next(my_gen))
print(next(my_gen))
print(next(my_gen))
print(next(my_gen))
print(next(my_gen))
print(next(my_gen))


# 2️⃣ Generator that processes data
def square_numbers(numbers):
    """Yields squares of given numbers."""
    for num in numbers:
        yield num ** 2

gen = square_numbers([1, 2, 3, 4])
print("Squared values:", list(gen))
# Output: [1, 4, 9, 16]

# 3️⃣ Using yield with condition
def even_numbers(limit):
    for i in range(limit + 1):
        if i % 2 == 0:
            yield i

print("Even numbers:", list(even_numbers(10)))
# Output: [0, 2, 4, 6, 8, 10]

# 4️⃣ Generator with multiple yield points
def greeting():
    yield "Hello"
    yield "from"
    yield "a generator!"

for word in greeting():
    print(word, end=" ")
print()
# Output: Hello from a generator!

# 5️⃣ Generator Expression (compact syntax)
gen_expr = (x ** 2 for x in range(5))
print("Generator expression output:", list(gen_expr))
# Output: [0, 1, 4, 9, 16]

# 6️⃣ Using 'yield from' to delegate to another generator
def sub_gen():
    yield 1
    yield 2

def main_gen():
    yield from sub_gen()
    yield 3

print("Yield from example:", list(main_gen()))
# Output: [1, 2, 3]

# 7️⃣ Generator with try/except (handling inside generator)
def safe_divisions(values):
    for a, b in values:
        try:
            yield a / b
        except ZeroDivisionError:
            yield "Division by zero!"

data = [(10, 2), (5, 0), (8, 4)]
print("Safe divisions:", list(safe_divisions(data)))
# Output: [5.0, 'Division by zero!', 2.0]

# 8️⃣ Infinite Generator (with break condition in loop)
def infinite_counter(start=0):
    while True:
        yield start
        start += 1

gen = infinite_counter()
print("First 5 from infinite generator:", [next(gen) for _ in range(5)])
# Output: [0, 1, 2, 3, 4]

# 9️⃣ Sending values into a generator
def accumulator():
    total = 0
    while True:
        value = yield total
        if value is None:
            break
        total += value

gen = accumulator()
print("Send to generator example:")
print(next(gen))       # Start the generator → 0
print(gen.send(10))    # Adds 10 → 10
print(gen.send(5))     # Adds 5  → 15
gen.close()
# Output: 0, 10, 15

# 🔟 Generator finalization with finally
def cleanup_gen():
    try:
        yield "Working..."
    finally:
        print("Generator cleanup executed!")

g = cleanup_gen()
print(next(g))
g.close()  # triggers finally block
# Output: "Working..." and then "Generator cleanup executed!"
