flooe=int(input("几层？"))
room=int(input("每层几间？"))
print("———"*room)
for i in range(flooe):
    for j in range(room):
        print("!_!",end="")
    print()
print("———"*room)