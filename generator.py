from sys import getsizeof

values = (x*2 for x in range(200000))
print(values)
print(getsizeof(values))

values = [x*2 for x in range(200000)]
print(getsizeof(values))
