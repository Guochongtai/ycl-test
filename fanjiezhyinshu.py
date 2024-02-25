def divprime(num):
    result=[]
    print(num,'=',end='')
    while num!=1:
        for i in range(2,int(num)):
            if int(num) % i==0:
                result.append(i)
                num=num/i
                break
    for i in range(0,len(result)-1):
        print(result[i],'*',end='')
        print(result[-1])
divprime(90)