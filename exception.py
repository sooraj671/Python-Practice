# try:
#     with open("sets.py") as file, open("game.py") as game:
#         print("file opened")
#         # context management protocol
#         # file.__enter__
#         # file.__exit__
#     age = int(input("Enter age:"))
#     xfactor = 10/age
# except (ValueError, ZeroDivisionError) :
#     print("Invalid input")
# else:
#     print("in else block")  
# # finally:
# #     file.close()
    
# print("outside")      


from timeit import timeit

code1 = """def calculate_xfactor(age):
    if age <= 0:
        raise ValueError("Invalid age.")
    return 10/age

try:
    calculate_xfactor(-1)
except ValueError as ex:
    pass
"""
    
timeit(code1, number=10000)


code2 = """def calculate_xfactor(age):
    if age <= 0:
        return None
    return 10/age

x = calculate_xfactor(-1) 
if x is None:
    pass
"""


print(timeit(code1, number=10000000000000))
print(timeit(code2, number=10000000000000))