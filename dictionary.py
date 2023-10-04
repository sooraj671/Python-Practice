point = {"x":1, "y":2}
print(point)
point = dict(x=1,y=10)
print(point)
point["z"] = 20
print(point)

if "x" in point:
    print(point["x"])
    
print(point.get("a",0))

del point["x"]
print(point)

for x, y in point.items():
    print(x, y)
    
values = {x:x*2 for x in range(5)}    

print(values)