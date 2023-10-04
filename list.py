letters = ["a","b","c"]
matrix = [[1,2],[2,3],[4,5]]
zeros = [0] * 5
combined = zeros + letters
numbers = list(range(20))
chars = list("Hello World")


print(matrix)
print(zeros)
print(combined)
print(numbers)
print(chars)
print(len(chars))

new_numbers = list(range(20))

print(new_numbers[::2])
print(new_numbers[::-1])

he,  *others, hi = new_numbers
print(he, hi)
print(others)

for index, letter in enumerate(letters):
    print(index, letter)
    
    
letters.append("d")

letters.insert(0,"-")

letters.pop()

letters.pop(2)    

# letters.remove("b")

# remove a range of item
del letters[0:3]

# clear all list
letters.clear()


print(letters.count("d"))
if "d" in letters:
    print(letters.index("d"))



num = [40,2,42,5,22,2,1]
num.sort(reverse=False)
print(num)
print(sorted(num, reverse=True))


items = [
         ("Product1", 20),
         ("Product2", 2),
         ("Product3", 12)]

# def sort_items(item):
#     return item[1]

# items.sort(key=sort_items)
items.sort(key=lambda item:item[1])
print(items)


prices = list(map(lambda item:item[1], items))
print(prices)

filtered = list(filter(lambda item: item[1] >= 10, items))
print(filtered)


new_prices = [item[1] for item in items]
print(new_prices)

new_filtered = [item for item in items if item[1]>=10]

print(new_filtered)