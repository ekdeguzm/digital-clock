# Importing the modules
import turtle
import time

# Creating the screen
wn = turtle.Screen()
wn.bgcolor("white")
wn.setup(width = 300, height = 200)
wn.title("First Digital Clock")
wn.tracer(0) # Do not want screen to flicker

# Creating the pens
# Pen 1
pen = turtle.Turtle() # Make sure that 2nd "T" in Turtle is capitalized
pen.speed(0)
pen.penup()
pen.hideturtle()

# Pen 2
pen2 = turtle.Turtle()
pen2.speed(0)
pen2.penup()
pen2.hideturtle()

# Pen 3
pen3 = turtle.Turtle()
pen3.speed(0)
pen3.penup()
pen3.hideturtle()

# Creating the functions
def draw_clock():
    pen.color("gray") # Spell gray not grey? test
    pen.pensize(7) # test
    x = pen.xcor = -75
    y = pen.ycor = 45
    pen.goto(x, y)
    pen.pendown()
    for s in range (2): # why 2?
        pen.forward(150) # test this
        pen.right(90) # test
        pen.forward(50) # test
        pen.right(90)
    pen.penup()
    pen2.color("black")
    pen2.pensize(25)
    pen2.goto(x - 15, y + 15)
    pen2.pendown()
    for i in range(2): # 2 because rectangle but how?
        pen2.forward(180)
        pen2.right(90) # is this angle change or how long the pen goes?
        pen2.forward(80)
        pen2.right(90)

def clockwork():
    pen3.color("red")
    pen3.goto(0,0)
    pen3.clear()
    pen3.write(h + ":" + m + ":" + s, font=("Courier", 25, "normal"), align = "center")
    pen3.penup()
    pen3.goto(0, -30)
    pen3.pendown()
    pen3.write(d, font=("Courier", 15, "normal"), align="center")

# Creating main loop
while True:
    # Set hours to 24 hour clock
    h = time.strftime("%H") # time.stringformattime %h = 24 clock %i = 12 hr clock
    m = time.strftime("%M")
    s = time.strftime("%S") # Why does S need to be capital?

    # Update the day
    d = time.strftime("%D")

    draw_clock()
    clockwork()

    wn.update() # updates the screen and the time

    time.sleep(1) # stops program for 1 sec then continues
# Keep the screen open
wn.mainloop()
        
        
    
    
