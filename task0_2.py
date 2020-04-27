num = int(input("Enter the value of n: "))
n = num
sum = 0
while num > 0:
    sum = sum + num
    num = num - 1
# displaying output
print("The sum of all number between 1 and", n, ": ", sum)