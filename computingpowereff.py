def pow(x,y):
    if y==0:
        return 1
    temp=pow(x,y//2)
    if y%2==0:
        return temp*temp
    else:
        return x*temp*temp
    
if __name__=="__main__":
    x=2
    y=3

    result=pow(x,y)
    print(result)
