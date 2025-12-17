def addDigits(num):
    while num>=10:
        tot=0
        while num>0:
            tot+=num%10
            num//=10
        num=tot    
    return num     
n=38
print(addDigits(n))