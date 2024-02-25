geshu=0
for shu in range(0,101):
    print("shu/4"+str(shu//4))
    print(shu%4)
    if shu%4==0:
        geshu+=1
print("有"+str(geshu)+"个数")