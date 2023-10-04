a=int(input("Enter the lower range:"))
b=int(input("Enter the upper range:"))
print("prime numbers in a given range")
for n in range(a,b+1):
        if n>1:
           for i in range(2,n):
             if(n%i)==0:
               break
           else:
                print(n)
