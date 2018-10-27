import turtle ,datetime
import turtle as t
a=0
def drawGap():
    t.penup()
    t.fd(5)
def drawLine(draw):
    drawGap()
    t.pendown()if draw else turtle.penup()
    t.fd(40)
    drawGap()
    turtle.right(90)
def drawDigit(d):
    global a
    drawLine(True) if d in [2,3,4,5,6,8,9] else drawLine(False)
    drawLine(True) if d in [0,1,3,4,6,7,8,9] else drawLine(False)
    drawLine(True) if d in [0,2,3,5,6,8,9] else drawLine (False)
    drawLine(True) if d in [0,2,6,8] else drawLine(False)
    t.left(90)
    drawLine(True) if d in [0,4,5,6,8,9] else drawLine(False)
    drawLine(True) if d in [0,2,3,5,6,7,8,9] else drawLine(False)
    drawLine(True) if d in [0,1,2,3,4,7,8,9] else drawLine(False)
    t.left(180)
    t.penup()
    t.fd(20)
    for a in range(a+1,8):
        if a == 1:
            t.pencolor("green")
            break
        elif a == 2:
            t.pencolor("red")
            break
        elif a == 3:
            t.pencolor("grey")
            break
        elif a == 4:
            t.pencolor("darkgreen")
            break
        elif a == 5:
            t.pencolor("gold")
            break
        elif a == 6:
            t.pencolor("violet")
            break
        elif a == 7:
            t.pencolor("purple")
            break
        elif a == 8:
            t.pencolor("orange")
            break
def drawDate(date):
    for i in date:
        if i== '-':
            t.write('年',font=("Arial",18,"normal"))
            t.fd(40)
        elif i=='=':
            t.write('月',font=("Arial",18,"normal"))
            t.fd(40)
        elif i=='+':
            t.write('日',font=("Arial",18,"normal"))
        else:
            drawDigit(eval(i))
def main():
    t.setup(800,350,200,200)
    t.penup()
    t.fd(-300)
    t.pensize(5)
    drawDate(datetime.datetime.now().strftime('%Y-%m=%d+'))
    t.hideturtle()
main()
