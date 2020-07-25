dic = {
    0:4,
    1:3,
    2:3,
    3:5,
    4:4,
    5:4,
    6:3,
    7:5,
    8:5,
    9:4,
    10:3,
    11:6,
    12:6,
    13:len("thirteen"),
    14:len("fourteen"),
    15:len("fifteen"),
    16:len("sixteen"),
    17:len("seventeen"),
    18:len("eighteen"),
    19:len("nineteen"),
    20:len("twenty"),
    30:len("thirty"),
    40:len("forty"),
    50:len("fifty"),
    60:len("sixty"),
    70:len("seventy"),
    80:len("eighty"),
    90:len("ninety")
}



def countNmberLetters(n):
    sum = 0

    if n >0 and n%100 == 0 and n!=1000:
        sum+=dic[n//100]
        sum+=len("hundred")
    elif len(str(n)) == 1:
        sum+=dic[n]
    elif len(str(n)) == 2:
        sum+=dic[n//10*10]
        if n%10 != 0:
            sum+=dic[n%10]
        else:
            sum+=dic[n%10]
    else:
        if n != 1000:
            sum+=dic[n//100]
            sum+=len("hundred")
            temp = n
            temp %= 100
            if temp>0:
                sum+=len("and")
            if temp//10*10 !=0:
                sum+=dic[temp//10*10]
            if temp%10 != 0:
                sum+=dic[temp%10]
        else:
            #space is not given because spaces are not counted.
            sum+=len("onethousand")
    return sum
    
def main(n):
    m = 1
    tSum = 0
    while m <= n:
        s=countNmberLetters(m)
        tSum+=s
        print(m,s,tSum)
        m+=1
    print(tSum)
    return

if __name__ == "__main__":
    main(1000)
