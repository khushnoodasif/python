n= int(input("Enter a number "))
for x in range(2,n):
    if n%x==0:
        break
if x+1==n:
    print (n,"is a prime number")
else:
    print (n,"is not a prime number")