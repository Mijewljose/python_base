m=int(input())
n=int(input())
min_value=min(m,n)
for i in range(1,min_value+1):
    if (m%i == 0 and n%i == 0):
        gcd=i
lcm = (m * n) // gcd
print(f"HCF={gcd} LCM={lcm}")
  
