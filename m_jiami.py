b26='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
s26='abcdefghijklmnopqrstuvwxyz'
n=3
mingwen='China'
anwen=''
for zifu in mingwen:
    if zifu in b26:
        i=0
        for b26_zifu in b26:
            if b26_zifu==zifu:
                anwen+=b26[(i+n)%26]
                break
            i+=1
    else:
        i=0
        for s26_zifu in s26:
            if s26_zifu==zifu:
                anwen+=s26[(i+n)%26]                
                break
            i+=1
print(anwen)