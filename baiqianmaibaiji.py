g=1
m=1
x=1
daan=False
for g in range(1,(100-1-3)//5):
    for m in range(1,(100-1-g*5)//3):
        x=(100-g*5+m*3)*3
        if g+m+x==100:
            daan=True
            break
    if daan==True:
        break
print('公鸡是:%d只,母鸡是:%d只,小鸡是:%d只'%(g,m,x))