#brute Force

from time import time

def chainGenerator(n):
    c = 1
    while True:
        if n%2 == 0:
            n=n/2
        else:
            n=3*n+1
        if n == 1:
            return c
        c+=1

def largestChain(n):
    lc = [0,0]
    while n>0:
        cg = chainGenerator(n)
        if cg > lc[0]:
            lc[0] =cg
            lc[1] = n
            #print(lc)
        n-=1
        
    return lc

def main():
    print("Answer")
    print(largestChain(1000000))
    print(startTime - time())

if __name__ == "__main__":
    startTime = time()
    main()


'''
Sol:
[152, 1000000]
[258, 999999]
[289, 999667]
[395, 999295]
[439, 997823]
[457, 970599]
[506, 939497]
[524, 837799]
[524, 837799]
first is the chain second is the value for that
'''