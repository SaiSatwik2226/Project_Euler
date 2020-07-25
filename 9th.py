#brute force
# a<b<c
# a = s/3  b=s/2
a=0
b=0

c= 0
s = 1000
# perimeter s = a+b+c
# c = s-a-b

for a in range(1,(int)(s/3)):
    for b in range(1,(int)(s/2)):
        c = s-a-b

        if a*a+b*b == c*c:
            print(a*b*c)
        else:
            continue

