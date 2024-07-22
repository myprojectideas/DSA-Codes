import math
def print_divisors(n):
    i=1
    while i*i<n:
        if n%i==0:
            print(i,end =" ")
        i+=1

    if i-(n//i)==1:
        i-=1

    while i>=1:
        if n%i==0:
            print(n//i,end=" ")
        i-=1


if __name__=="__main__":
    print("The divisors of 100 are:")
    print_divisors(100)