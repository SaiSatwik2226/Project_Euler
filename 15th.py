from math import factorial

'''
in any n*m grid if one has to move from one corner to the other then he should move n times right and m times down.

the number of ways it can be done is (n+m)! factorial but the consraits are it should move right and down only so,
divinded by n! and m!

which comes out to be,
(n+m)!/n!*m!

i.e. (m+n)Cn
binomial coefficient
'''
from time import time

def noOfWays(n,m):
    return factorial(n+m)/(factorial(m)*factorial(n))

def main(n,m):
    print(noOfWays(n,m))
    print(time() - startTime)
    return

if __name__ == "__main__":
    startTime = time()
    main(20,20)