values = [1,2,3]
print(values)
print(*values)

numbers = list(range(5))
print(numbers)
numbers = [*range(5), *"Hello Sooraj", 9,20]
print(numbers)


first = {"x":1}
second = {"x": 10, "y":20}
third = dict(y=30, z=90)


combined = {**first, **second, **third}

print(combined)
