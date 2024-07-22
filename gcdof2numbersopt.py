def gcd(a,b):
    return a if b==0 else gcd(b,a%b)

a=98
b=56

print(f"GCD of {a} and {b} is {gcd(a,b)}")