from random import *
print("---------欢迎来到极客梦想的世界----------")
blood=randint(80,150)
attack=randint(10,30)
defense=randint(40,80)
combat=(blood+attack*6+defense*2)/3
print("您的攻击值为："+str(attack))
print("您的防御值为："+str(defense))
if combat>=130:
    print("您的战力值居然是"+str(combat)+"，大佬，带带我")
elif combat<130 and combat>=80:
    print("您的战力值是"+str(combat)+"继续加油")
else:
    print("您的战力值是"+str(combat)+"天呐，你直接删号重开吧！")