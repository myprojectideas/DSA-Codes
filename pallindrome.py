def checkPalindrome(n):
    reverse=0
    temp=n
    while(temp!=0):
        reverse=(reverse*10)+(temp%10)
        temp=temp//10

    

    return (reverse==n)

n=111
if(checkPalindrome(n)==1):
        
        print("Yes")

else:
        
        print("No")

