# FizzBuzz
# We can use modulo % like in JS
# Python uses == for comparison
# if, elif else statements are followed by colons
# indentation decides the scope, not curly braces


def FizzBuzz(n):
    if n % 15==0:
        # I'm in this block!
        return "FizzBuzz"
    elif n % 5==0:
        return "Buzz"
    elif n % 3==0:
        return "Fizz"
    else: 
        return n

# this is one example of a for loop using the range function. 
# range(100) will give us 0,1,2,3...98,99 
for x in range(100):
    print(FizzBuzz(x))