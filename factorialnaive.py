def factorial(n):
    if n==0 or n==1:
        return 1
    return n*factorial(n-1)

def main():
    num=5
    print(f"factorial of {num} is {factorial(num)}")

if __name__=="__main__":
    main()

