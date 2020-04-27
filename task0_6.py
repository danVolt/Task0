import math
def perfectsq(u):
    v=int(math.sqrt(u))
    return v*v == u
def fibonacci(i):
    return perfectsq(5*i*i + 4) or perfectsq(5*i*i - 4)
m=0
n=1
i=0
print("Fibonacci Series:")
print(m)
print(n)
while i<6:
    m=m+n
    print(m)
    n=m+n
    print(n)
    i=i+1
print("\n \nFIBONACCI NUMBER CHECK")
x=int(input("Enter a number: "))
if(fibonacci(x) == True):
    print("It is a Finacci number.")
else:
    print("It is not a Finacci number.")

