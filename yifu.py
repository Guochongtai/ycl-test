gao=int(input("您的身高是？(cm)"))
if gao<=165:
    print("您应该穿S号衣服")
elif gao<=170 and gao>165:
    print("您应该穿M号衣服")
elif gao<=175 and gao>170:
    print("您应该穿L号衣服")
elif gao<=180 and gao>175:
    print("您应该穿XL号衣服")
else:
    print("您好高啊!您应该穿XXL号衣服")