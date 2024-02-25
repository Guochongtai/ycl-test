result=[]
for t in range(2,300,7):
    if t%3==2 and t%5==3:
        result.append(t)

print(result)