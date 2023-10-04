numbers = [1,2,3,1]
print(numbers)
first = set(numbers)
print(first)

second = {1,4}

print(first | second)
print(first & second)
print(first - second)
print(first ^ second)


if 1 in first:
    print("Yes")