import turtle ,datetime
import turtle as t
def drawLine(draw):
    t.pendown()if draw else turtle.penup()
    t.fd(40)
    turtle.right(90)
def drawDigit(d):
    t.pencolor("red")
    drawLine(True) if d in [2,3,4,5,6,8,9] else drawLine(False)
    t.pencolor("gold")
    drawLine(True) if d in [0,1,3,4,6,7,8,9] else drawLine(False)
    t.pencolor("black")
    drawLine(True) if d in [0,2,3,5,6,8,9] else drawLine (False)
    t.pencolor("violet")
    drawLine(True) if d in [0,2,6,8] else drawLine(False)
    t.left(90)
    t.pencolor("purple")
    drawLine(True) if d in [0,4,5,6,8,9] else drawLine(False)
    t.pencolor("green")
    drawLine(True) if d in [0,2,3,5,6,7,8,9] else drawLine(False)
    t.pencolor("blue")
    drawLine(True) if d in [0,1,2,3,4,7,8,9] else drawLine(False)
    t.left(180)
    t.penup()
    t.fd(20)
def drawDate(date):
    for i in date:   
        drawDigit(eval(i))
def main():
    t.setup(800,350,200,200)
    t.penup()
    t.fd(-300)
    t.pensize(5)
    drawDate(datetime.datetime.now().strftime('%Y%m%d'))
    t.hideturtle()
main()
    
