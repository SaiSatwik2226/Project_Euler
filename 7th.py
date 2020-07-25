from math import sqrt

def prime(n):
    if n <=1:
        return False
    for i in range(2,int(sqrt(n))+1):
        if n%i == 0:
            return False
    return True
    


c = 0
n = 1
while c != 10001:
    if prime(n):
        c +=1
    n += 1

print(n-1)