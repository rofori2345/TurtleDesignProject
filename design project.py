
import turtle
turtle.colormode(255)

turtle.bgcolor(0,0,0)
bob=turtle.Turtle()

bob.speed(100)








for times in range(180):

    bob.right(150)
    bob.circle(20)
    bob.right(200)
    bob.width(5)
    bob.begin_fill()
    bob.color(0,times,times)
    bob.end_fill()
    bob.right(250+1)
    bob.forward(200)
    bob.color(times,times,0)
    bob.circle(70)
    bob.forward(100)

    
    

    






 
            
