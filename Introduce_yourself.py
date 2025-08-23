def intro(name):
    print("Hello, Good morning! I am", name)
user_name = input("Enter your name")
intro(user_name)

def recur_factorial(n):
    if n==1:
        return n
    else :
        return n*recur_factorial
num = int(input("Enter a number"))
if num < 0:
    print("Sorry, factorial does not exist for negative numbers.")
elif num ==0:
    print("The factorial of 0 is 1")
else:
    print("The factorial of", num, "is", recur_factorial(num))