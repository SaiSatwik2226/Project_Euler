#brute force

from math import sqrt

def prime(n):
    if n <=1:
        return False
    for i in range(2,int(sqrt(n))+1):
        if n%i == 0:
            return False
    return True
    

c=0
sum = 0

while c != 2000000:
    if prime(c):
        sum+=c
    c+=1

print(sum)