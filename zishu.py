zifu=""
c=0
i=1
for s in zifu:
    for word in s:
        if word!='；':
            c+=1
print("共"+str(c)+"个字")