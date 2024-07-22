def count_digit(n):
    if n==0:
        return 1
    count=0
    while n!=0:
        n=n//10
        count+=1
    return count

def main():
    n=123354646
    print(f"Number of digits :{count_digit(n)}")

if __name__=="__main__":
    main()

 