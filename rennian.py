nianfen=int(input("输入想测试的年份:"))
nianfen2=str(nianfen)
if nianfen2[-1]==0 and nianfen2[-2]:
    if nianfen%400==0:
        print("是闰年")
    else:
        print("不是闰年")
elif nianfen%4==0:
    print("是闰年")
else:
    print("不是闰年")