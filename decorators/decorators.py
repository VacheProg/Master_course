# ============================================
# Python Decorators Examples (No functools.wraps)
# Covers basic, argumented, multiple, class-based,
# and practical decorators
# ============================================


import time


def simple_decorator(func):
    def wrapper():
        print("Before function runs")
        func()
        print("After function runs")
    return wrapper

@simple_decorator
def greet():
    print("Hello, World!")


print("Basic decorator example:")
greet()


raise  Exception()



# Output:
# Before function runs
# Hello, World!
# After function runs

# 2️⃣ Decorator for functions with argumen
print("\nDecorator with arguments:")
add(5, 3)
# Output shows logging of arguments and result

# 3️⃣ Decorator with arguments (decorator factory)
def repeat(n):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for i in range(n):
                print(f"Run {i + 1}/{n}:")
                func(*args, **kwargs)
        return wrapper
    return decorator

@repeat(3)
def say_hi():
    print("Hi there!")

print("\nDecorator with arguments:")
say_hi()
# Output: repeats function 3 times

# 4️⃣ Multiple decorators applied
def uppercase(func):
    def wrapper():
        result = func()
        return result.upper()
    return wrapper

def exclaim(func):
    def wrapper():
        result = func()
        return result + "!"
    return wrapper

@exclaim
@uppercase
def message():
    return "python decorators are cool"

print("\nMultiple decorators applied:")
print(message())

# 6️⃣ Practical example: timing decorator
import time

def timer(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"{func.__name__} executed in {end - start} seconds")
        return result
    return wrapper

@timer
def slow_operation():
    time.sleep(1)
    return "Done!"

print("\nTiming decorator example:")
print(slow_operation())
# Output: shows execution time

# 7️⃣ Practical example: access control (conditional decorator)
def requires_admin(func):
    def wrapper(user_role):
        if user_role != "admin":
            print("Access denied!")
            return
        return func(user_role)
    return wrapper

@requires_admin
def delete_database(user_role):
    print("Database deleted successfully!")

print("\nAccess control decorator example:")
delete_database("guest")   # Access denied
delete_database("admin")   # Executes

# ✅ Summary: Demonstrates
# - Basic decorators
# - Decorators with arguments
# - Nested and multiple decorators
# - Class-based decorators
# - Real-world use cases (timing, access control)
