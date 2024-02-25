zongfen=0
shu=int(input("您要算几个成绩的平均分\n"))
for c in range(shu):
    zongfen+=float(int(input("第"+str(c+1)+"个分数是多少？\n")))
pingjunfen=zongfen/shu
print(pingjunfen)