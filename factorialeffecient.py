def factorial(n):
    res=1
    for i in range(2,n+1):
        res*=i
    return res

def main():
    num=5
    print(f"factorial of {num} is {factorial(num)}")

if __name__=="__main__":
    main()
    