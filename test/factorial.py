def fact(n):
    if(n==0):
        return 1
    else:
        return n*fact(n-1)
num = int(input())
print(fact(n))

#without function

num= int(input())
fact=1
for i in range(1,n+1):
    fact=fact*i
print(f"factorial of {n} is {fact}")
