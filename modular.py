def mod_power(x,n,m):
    if n==0:
        return 1%m
    u=mod_power(x,n//2,m)
    u=(u*u)%m
    if n%2==1:
        u=(u*x)%m

    return u


if __name__=="__main__":
    print(mod_power(5,2,7))
    