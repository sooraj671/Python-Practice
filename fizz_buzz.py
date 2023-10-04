def fiz_buz(input):
    if(input % 5 == 0 and input % 3 == 0):
        return "FizzBuzz"
    elif(input % 3 == 0):
        return "Fizz"
    elif(input % 5 ==0):
        return "Buzz"
    else:
        return input

print(fiz_buz(2))