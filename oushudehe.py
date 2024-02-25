shu=1
he=0
while shu<=100:
    if shu%2==0:
        he+=shu
    shu+=1
else:
    print("和是"+str(he))