def find_trailing_zero(n):
    if n<0:
        return -1
    count=0
    i=5
    while n/i>=1:
        count+=n//i
        i*=5

    return count


if __name__=="__main__":
    n=100
    print("Count of trailing 0s in" ,n, "! is" , find_trailing_zero(n))