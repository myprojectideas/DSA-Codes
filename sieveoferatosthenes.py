def s_o_e(n):
    prime=[True for _ in range(n+1)]
    p=2

    while p*p<=n:
        if prime[p]:
            for i in range(p*p , n+1,p):
                prime[i]=False
        p+=1


    for p in range(2,n+1):
        if prime[p]:
            print(p,end=" ")

if __name__=="__main__":
    n=30
    print(f"Following are the prime numbers smaller than or equal to {n}:")
    s_o_e(n)