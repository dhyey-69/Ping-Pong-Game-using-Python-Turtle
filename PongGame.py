import turtle

a="DHYEY"
b="AIM"
smile="\U0001f604"
cry="\U0001F622"
score_pa=0
score_pb=0

po=turtle.Screen()
po.title("Pong Game by Dhyey")
po.bgcolor("black")
po.setup(width=800,height=600)
po.tracer(0)#stop screen to updated

#Player A
pa=turtle.Turtle()
pa.speed(0)
pa.shape("square")
pa.color("white")
pa.penup()
pa.goto(-350,0)
pa.shapesize(stretch_wid=5,stretch_len=1)

#Player B
pb=turtle.Turtle()
pb.speed(0)
pb.shape("square")
pb.color("white")
pb.penup()
pb.goto(350,0)
pb.shapesize(stretch_wid=5,stretch_len=1)

#Ball
ball=turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("white")
ball.penup()
ball.goto(0,0)
ball.dx=0.6
ball.dy=-0.6

#Score-Board
sb=turtle.Turtle()
sb.speed(0)
sb.color("white")
sb.penup()
sb.hideturtle()
sb.goto(0,260)
sb.write("{}:{}\t\t\t{}:{}".format(a,score_pa,b,score_pb),align="center",font=("Courier",20,"normal"))

#Emoji-1
emo1=turtle.Turtle()
emo1.speed(0)
emo1.color("white")
emo1.penup()
emo1.hideturtle()
emo1.goto(0,260)
emo1.write(" ")

#Emoji-2
emo2=turtle.Turtle()
emo2.speed(0)
emo2.color("white")
emo2.penup()
emo2.hideturtle()
emo2.goto(0,260)
emo2.write(" ")



def pa_up():
    y_a_up = pa.ycor()
    y_a_up += 20
    pa.sety(y_a_up)

def pa_down():
    y_a_down = pa.ycor()
    y_a_down -= 20
    pa.sety(y_a_down)

def pb_up():
    y_b_up = pb.ycor()
    y_b_up += 20
    pb.sety(y_b_up)

def pb_down():
    y_b_down = pb.ycor()
    y_b_down -= 20
    pb.sety(y_b_down)

po.listen()
#Moving Player-A
po.onkeypress(pa_up,"z")
po.onkeypress(pa_down,"x")

#Moving Player-B
po.onkeypress(pb_up,"Up")
po.onkeypress(pb_down,"Down")


while True:
    po.update()

    if(score_pa>=5):
            while(True):
                emo1.clear()
                emo1.goto(-200,-75)
                emo1.write("{}".format(smile),font=("Courier",100,"normal"))
                emo2.clear()
                emo2.goto(200,-75)
                emo2.write("{}".format(cry),font=("Courier",100,"normal"))
                sb.clear()
                sb.goto(0,260)
                sb.write("Winner:-{}".format(a),align="center",font=("Courier",20,"normal"))
            break
    if(score_pb>=5):
            while(True):
                emo1.clear()
                emo1.goto(-200,-75)
                emo1.write("{}".format(cry),font=("Courier",100,"normal"))
                emo2.clear()
                emo2.goto(200,-75)
                emo2.write("{}".format(smile),font=("Courier",100,"normal"))
                sb.clear()
                sb.goto(0,260)
                sb.write("Winner:-{}".format(b),align="center",font=("Courier",20,"normal"))
            break
    
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)


    #When ball touches Top of Screen
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1
    #When ball touches Bottom of Screen
    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1
    #When ball touches Left side(Behind Player-A) of Screen
    if ball.xcor() < -390:
        ball.goto(0,0)
        ball.dx *= -1
        score_pb += 1
        sb.clear()
        sb.write("{}:{}\t\t\t{}:{}".format(a,score_pa,b,score_pb),align="center",font=("Courier",20,"normal"))
    #When ball touches Right side(Behind Player-B) of Screen
    if ball.xcor() > 390:
        ball.goto(0,0)
        ball.dx *= -1
        score_pa += 1
        sb.clear()
        sb.write("{}:{}\t\t\t{}:{}".format(a,score_pa,b,score_pb),align="center",font=("Courier",20,"normal"))
    #When ball touches Player-A
    if (ball.xcor() < -340 and ball.xcor() > -350) and (ball.ycor() < pa.ycor() + 50 and ball.ycor() > pa.ycor() - 50):
        ball.setx(-340)
        ball.dx *= -1
    #When ball touches Player-B
    if (ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor() < pb.ycor() + 50 and ball.ycor() > pb.ycor() - 50):
        ball.setx(340)
        ball.dx *= -1