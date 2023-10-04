# and
# or
# not

name = "sooraj"

if not name:
    print("Name is empty")
    
name = " "

if not name:
    print("Name is empty")
    
    
name = " "

if not name.strip():
    print("Name is empty")    

age = 22

if 18 <= age < 30:
    message = "eligible"
    print("you are eligible")
    
if age >= 18 and age < 65:
    message = "eligible"
    print("yes you are eligible")    

print(message)


new_msg = "new_elgible" if age >=18 else "not_elgible" 

print(new_msg)
    
    