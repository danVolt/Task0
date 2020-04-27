n=int(input("Enter a no: "))
di=0
while n>0:
    n//=10
    di=di+1
print("Digit: ",di)
