def subtractProductAndSum(n):
    summ=0
    product=1
    while n>0:
        digit=n%10
        summ=summ+digit   
        product=product*digit
        n=n//10
    return product-summ

n=234
print(subtractProductAndSum(n))