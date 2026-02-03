# 1
t1 = (1, 2, 3)
t2 = (4, 5, 6)

result = tuple(a * b for a, b in zip(t1, t2))

print(result)


# 2
t = (1, 2, 3, 4)

result = t[::-1]

print(result)


# 3
t = ("salom", 123, "dunyo", 45.6, "!")

result = "".join(x for x in t if isinstance(x, str))

print(result)


# 4
t = (10, 3, 7, 25, 3)

# Faqat sonlarni topish
numbers = [x for x in t if isinstance(x, (int, float))]

if numbers:
    min_val = min(numbers)
    max_val = max(numbers)
    min_index = t.index(min_val)
    max_index = t.index(max_val)
    print(f"Eng kichik: {min_val} (indeks {min_index})")
    print(f"Eng katta: {max_val} (indeks {max_index})")
else:
    print("Tuple ichida son yo'q")
