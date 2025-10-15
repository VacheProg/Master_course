# ============================================
# Python Exception Handling Examples
# Covers all major try/except use cases
# ============================================

# 1️⃣ Basic try/except
try:
    print("Dividing by zero...")
    a = 10
    b = 0
    if b == 0:
        raise  ZeroDivisionError("")

    a/b
    result = 10 / 0

except ZeroDivisionError as esiminch:
    print("Caught ZeroDivisionError!")
except ArithmeticError:
    print('another arithmetic error')
except Exception as why:
    print(why)

try:
    a = int(input())
except ValueError:
    print("please input valid integer")
# 2️⃣ Catching multiple specific exceptions
try:
    value = int("abc")  # ValueError
    lst = [1, 2, 3]
    print(lst[5])       # IndexError
except (ValueError, IndexError) as e:
    print(f"Caught either ValueError or IndexError: {e}")

# 3️⃣ Catching all exceptions (generic)
try:
    x = 10 / 0
except Exception as e:
    print(f"Caught a general exception: {e}")

# 4️⃣ Using else (runs only if no exception)
try:
    num = int("5")
except ValueError:
    print("Invalid number!")
else:
    print(f"Conversion successful: {num}")

# 5️⃣ Using finally (always runs)
try:
    print("Opening file...")
    f = open("nonexistent.txt", "r")
except FileNotFoundError:
    print("File not found!")
finally:
    print("This always runs (cleanup, closing files, etc.)")

# 6️⃣ Nested try/except
try:
    print("Outer try block")
    try:
        print("Inner try block")
        x = 10 / 0
    except ZeroDivisionError:
        print("Handled inside inner block")
    print("Continuing outer block...")
    int("abc")
except ValueError:
    print("Handled in outer block")

# 7️⃣ Raising exceptions manually
try:
    raise RuntimeError("Something went wrong intentionally!")
except RuntimeError as e:
    print(f"Caught manually raised error: {e}")

# 8️⃣ Dictionary key error example
try:
    data = {"name": "Alice", "age": 25}
    print("Accessing nonexistent key...")
    print(data["address"])  # KeyError
except KeyError as e:
    print(f"Caught KeyError: Missing key {e}")

# 9️⃣ Set operation causing exception (like removing missing item)
try:
    s = {1, 2, 3}
    print("Removing item not in set...")
    s.remove(5)  # KeyError
except KeyError as e:
    print(f"Caught KeyError while removing from set: {e}")

# 🔟 Exception chaining (raise from)
try:
    try:
        int("abc")
    except ValueError as e:
        raise TypeError("Type issue occurred!") from e
except Exception as e:
    print(f"Exception chaining example: {e.__class__.__name__} caused by {e.__cause__.__class__.__name__}")

# 11️⃣ Using assert and catching AssertionError
try:
    assert 2 + 2 == 5, "Math is broken!"
except AssertionError as e:
    print(f"Caught assertion error: {e}")

def a(my_list):
    assert len(my_list) > 100, "not enough"


