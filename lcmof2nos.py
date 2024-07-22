def gcd(a,b):
    if b==0:
        return a
    return gcd(b,a%b)

def lcm(a,b):
    return (a*b)//gcd(a,b)

def main():
    a=7
    b=35

    print(f"LCM of {a} and {b} is {lcm(a,b)}")

if __name__=="__main__":
    main()