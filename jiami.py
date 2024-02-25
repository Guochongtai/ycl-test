b26='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
s26='abcdefghijklmnopqrstuvwxyz'
n=3
mingwen="China"
anwen=""
for zifu in mingwen:
    if zifu in b26:
        i=0
        for zifu2 in b26:
            if zifu2==zifu:
                anwen+=b26[(i+n)%26]
                break
            i+=1
    else:
        i=0
        for zifu3 in s26:
            if zifu3==zifu:
                anwen+=s26[(i+n)%26]
                break
            i+=1
print(anwen)