from random import*
z号码=randint(0,11)
g号码=input("您好，我们正在举行抽奖活动\n请您输一个数字作为号码(1~10)")
if z号码==int(g号码):
    print('中奖了!')
else:
    print('没抽中，中奖号码是'+str(z号码))