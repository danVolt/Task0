n=int(input("Enter a no: "))
n=n+1
i=1
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
print("Prime numbers are : ")
while i<n:
    prime(m[i])
    i=i+1