from time import *
from random import *

yx=randint(80,150)
yg=randint(10,20)
yf=randint(40,80)
rx=randint(80,150)
rg=randint(10,20)
rf=randint(40,80)

print("展示双方战力值")
print("我方战力值为:")
print("血量:"+str(yx))
sleep(1)
print("攻击值:"+str(yg))
sleep(1)
print("防御值:"+str(yf))
sleep(1)
print("敌方战力值为:")
print("血量:"+str(rx))
sleep(1)
print("攻击值:"+str(rg))
sleep(1)
print("防御值:"+str(rf))
sleep(1)

print("战斗开始")
yx=yx-(yx/(yx+yf))*rg
rx=rx-(rx/(rx+rf))*yg
print("敌方发动攻击，我方剩余血量为",int(yx))
print("我方发动攻击，敌方剩余血量为",int(rx))

if yx>rx:
    print("我们赢了！")
elif yx<rx:
    print("我们输了！")
elif yx==rx:
    print("平局！")