a=int(input("Enter a number:"))
def factorial(a):
    if a<=1:
        return 1
    else:
        return a*factorial(a-1)
c=factorial(a)
print("Factorial of "+str(a)+ " is:",c)
