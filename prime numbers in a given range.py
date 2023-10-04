a=int(input("Enter first number:"))
b=int(input("Enter the last number:"))
print("prime numbers in a given range:")
for n in range(a,b+1):
        if n>1:
           for i in range(2,n):
             if(n%i)==0:
               break
           else:
                print(n)

    
