print("ENTER THE INTERVAL: ")
i=int(input("Enter the first number of the interval: "))
n=int(input("Enter the last number of the interval: "))
n=n+1
m=range(n)
def prime(x):
    y=x//2
    t=0
    while y>1:
        z=x%y
        if z==0:
            t=1
        y=y-1
    if t==0:
        print(x)
print("Prime numbers in the given interval : ")
for e in range(i, n):
    prime(m[e])

q=int(input("Insert a number to check whether it is prime or not: "))
l=q//2
c=0
while l>1:
    z=q%l
    if z==0:
        c=1
    l=l-1
if c==0:
    print(q," is a prime number.")
else:
    print(q," is not a prime number.")