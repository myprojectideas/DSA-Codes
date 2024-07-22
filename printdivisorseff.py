import math
def print_divisors(n):
    for i in range (1,int(math.sqrt(n))+1):
        if n%i==0:
            if n//i==i:
                print(i, end=" " )

            else:
                print(i,n//i,end=" ")

if __name__=="__main__":
    print("The divisors of 100 are:")
    print_divisors(100)
