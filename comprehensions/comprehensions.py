# ============================================
# Python Comprehension Examples
# Covers list, dict, set, and generator comprehensions
# ============================================

# 1️⃣ Basic List Comprehension
numbers = [1, 2, 3, 4, 5]
squares = [n ** 2 for n in numbers]

print("List of squares:", squares)
# Output: [1, 4, 9, 16, 25]

# 2️⃣ List Comprehension with Condition (filtering)
even_numbers = [n*j for n in numbers for j in range(10) if n % 2 == 0]
print("Even numbers:", even_numbers)
# Output: [2, 4]

# 3️⃣ List Comprehension with if-else (value selection)
labels = ["even" if n % 2 == 0 else "odd" for n in numbers]
print("Even/Odd labels:", labels)
# Output: ['odd', 'even', 'odd', 'even', 'odd']

# 4️⃣ Nested List Comprehension (2D flattening)
matrix = [[1, 2], [3, 4], [5, 6]]
flattened = [x for row in matrix for x in row]
print("Flattened matrix:", flattened)
# Output: [1, 2, 3, 4, 5, 6]

# 5️⃣ Dictionary Comprehension
students = ["Alice", "Bob", "Charlie"]
scores = [85, 90, 78]
student_scores = {name: score for name, score in zip(students, scores)}
print("Dictionary comprehension:", student_scores)
# Output: {'Alice': 85, 'Bob': 90, 'Charlie': 78}

# 6️⃣ Dictionary Comprehension with Condition
high_scorers = {name: score for name, score in student_scores.items() if score >= 85}
print("Filtered dictionary (score >= 85):", high_scorers)
# Output: {'Alice': 85, 'Bob': 90}

# 7️⃣ Set Comprehension
unique_squares = {n ** 2 for n in [1, 2, 2, 3, 3, 3, 4]}
print("Set comprehension (unique squares):", unique_squares)
# Output: {16, 1, 4, 9}

# 8️⃣ Set Comprehension with Condition
odd_squares = {n ** 2 for n in numbers if n % 2 == 1}
print("Odd number squares:", odd_squares)
# Output: {1, 9, 25}

# 9️⃣ Generator Comprehension (lazy evaluation)
generator = (n ** 2 for n in range(5))
print("Generator object:", generator)
print("Generated values:", list(generator))
# Output: [0, 1, 4, 9, 16]

# 🔟 Nested Generator Example
matrix = [[1, 2, 3], [4, 5, 6]]
gen = (x for row in matrix for x in row if x % 2 == 0)
print("Even numbers from matrix:", list(gen))
# Output: [2, 4, 6]

# 11️⃣ Real-world List Comprehension (string processing)
words = ["Python", "is", "great"]
upper_words = [word.upper() for word in words]
print("Uppercased words:", upper_words)
# Output: ['PYTHON', 'IS', 'GREAT']

# 12️⃣ Combining Enumerate and Comprehension
indexed = {i: word for i, word in enumerate(words)}
print("Enumerated dictionary:", indexed)
# Output: {0: 'Python', 1: 'is', 2: 'great'}

