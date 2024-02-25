from random import *
print("欢迎来到猜拳游戏")
zq=choice(['石头','剪刀','布'])
yq=input("请出拳\n")
if zq=="石头" and yq=='石头':
    print(zq)
    print("平局，这节奏不要停，决战到天亮")
if zq=="剪刀" and yq=='剪刀':
    print(zq)
    print("平局，这节奏不要停，决战到天亮")
if zq=="布" and yq=='布':
    print(zq)
    print("平局，这节奏不要停，决战到天亮")
if zq=="石头" and yq=='剪刀':
    print(zq)
    print("输了，调试一下，再战。")
if zq=="布" and yq=='石头':
    print(zq)
    print("输了，调试一下，再战。")
if zq=="剪刀" and yq=='布':
    print(zq)
    print("输了，调试一下，再战。")
if zq=="石头" and yq=='布':
    print(zq)
    print("赢了，厉害！")
if zq=="剪刀" and yq=='石头':
    print(zq)
    print("赢了，厉害！")
if zq=="布" and yq=='剪刀':
    print(zq)
    print("赢了，厉害！")
