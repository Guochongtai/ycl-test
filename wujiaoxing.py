from turtle import *
color=('red','blue')
ht()
begin_fill()
while True:
    fd(200)
    rt(144)
    if abs(pos())<1:
        break
end_fill()
done()