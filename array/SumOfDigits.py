#iterative 
def getSum(n):
    sum = 0
    while(n!=0):
        sum = sum + int(n%10)
        n = int(n/10)

    return sum

n = 123
print(getSum(n))

#Recursive
def gettSum(n):
    return 0 if n==0 else int(n%10)+gettSum(int(n/10))

n = 123
print(gettSum(123))
