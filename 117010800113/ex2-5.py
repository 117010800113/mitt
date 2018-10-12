from turtle import*
while True:
    fd(250)
    left(120)
    if abs(pos())<1:
        break
fd(125)
seth(60)
while True:
    fd(125)
    left(120)
    if abs(pos())<125:
        break
