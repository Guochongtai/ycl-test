def duobianxing():
    bianchangshu2=1
    zhouchang=0
    print("我会求多边形的周长。")
    bianchangshu=input("它有几条边？")
    #while bianchangshu2<=int(bianchangshu):
     #   zhouchang+=int(input("第"+str(bianchangshu2)+"长多少?"))
      #  bianchangshu2+=1
    for bianchangshu3 in range(1,(int(bianchangshu)+1)):
        zhouchang+=int(input("第"+str(bianchangshu3)+"长多少?"))

    print(int(zhouchang))
    return int(zhouchang)
#duobianxing()
