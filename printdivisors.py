def print_divisors(n):
    for i in range (1,n+1):
        if n%i==0:
            print(i, end=" ")

if __name__=="__main__":
    print("The divisors of 100 are:")
    print_divisors(100)
