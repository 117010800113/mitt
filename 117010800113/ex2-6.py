from turtle import*
while True:
    fd(100)
    penup()
    fd(25)
    left(90)
    fd(25)
    pendown()
    if abs(pos())<1:
        break
