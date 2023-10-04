# def increment(number:int, by:int=1) -> tuple:
#  return (number,number+by)

# print(increment(2,2))


def multiply(*list):
    total = 1
    for x in list:
        total *= x
    return total

print(multiply(2,3,4,5))



def save_users(**users):
 print(users["name"])
 
save_users(id=1, name="sooraj")


message = "hello"

def greet():
    # this is a bad practice
    global message 
    message = "world"
    print(message)
    
greet()
print(message)