from graphics import *
import random as ran

pitching = False

offscreen = False

playing = True

hit = False

batting = False


def main():

    window = GraphWin("PythonBaseball", 500, 500)

    window.setBackground(color_rgb(92, 149, 58))



    while(playing):

        FieldDraw(window)
        Batter(window)
        Pitcher(window)
        pitchButton(window)


def FieldDraw(Window):
    mound = Oval(Point(210, 230), Point(290, 285))
    mound.setFill(color_rgb(148, 129, 67))

    mound2 = Oval(Point(180, 400), Point(330, 450))
    mound2.setFill(color_rgb(148, 129, 67))
    mound2.draw(Window)
    mound.draw(Window)

def pitchButton(Window):
    button = Rectangle(Point(1,2),Point(150,50))
    button.setFill(color_rgb(186, 43, 43 ))
    text = Text(Point(75,25),"PITCH!!")
    text.setFill('black')
    text.setFace('arial')
    text.setSize(25)
    button.draw(Window)
    text.draw(Window)
    mouse = Window.getMouse()
    if(mouse.x > 1 and mouse.x < 150 and mouse.y > 2 and mouse.y < 50):
       (globals()[('pitching')]) = True

def Pitcher(Window):

    #Head
    point = Point(250,175)
    Head = Circle(point,10)
    Head.setFill('black')
    #Body
    Body = Line(Point(250,175),Point(250,220))
    Body.setFill('black')
    #Legs
    Legs = Line(Point(250, 220), Point(260, 260))
    Legs.setFill('black')
    Legs1 = Line(Point(250, 220), Point(240, 260))
    Legs1.setFill('black')

    Legs1.draw(Window)
    Legs.draw(Window)
    Body.draw(Window)
    Head.draw(Window)

    if(globals()['pitching'] == False):
        Arms = Line(Point(250, 190), Point(260, 220))
        Arms.setFill('black')
        Arms1 = Line(Point(250, 190), Point(240, 220))
        Arms1.setFill('black')
        Arms1.undraw()
        Arms.draw(Window)
        Arms1.draw(Window)

    else:
        Arms = Line(Point(250, 190), Point(260, 220))
        Arms.setFill('black')
        Arms1 = Line(Point(250, 190), Point(230, 170))
        Arms1.setFill('black')

        Arms.draw(Window)
        Arms1.draw(Window)
        time.sleep(2)
        Arms1.undraw()
        Arms1 = Line(Point(250, 190), Point(230, 220))
        Arms1.setFill('black')
        Arms1.draw(Window)
        baseballMoving(Point(230, 170),5,Window)
    Arms1.undraw()



def baseballMoving(point,radius,Window):
    ball = Circle(point,radius)
    ball.setFill('white')
    ball.draw(Window)
    speed = generatePitch()
    curve = generateCurve()

    while(globals()['pitching']):

        print(speed)
        print(curve)
        ball.move(curve, speed)
        curve = curve + 0.000002
        if(ball.getCenter().y > 480 ):
            globals()['pitching'] = False
            ball.undraw()

        if (Window.lastKey == "space"):

            globals()['batting'] = True
        else:
            globals()['batting'] = False

    if(hit):
        while(ball.getCenter() > 0):
            ball.move(0,-0.2)
bat2drawing = False
def Batter(Window):
    # Head
    point = Point(300, 335)
    Head = Circle(point, 10)
    Head.setFill('black')
    # Body
    Body = Line(Point(300, 335), Point(300, 395))
    Body.setFill('black')
    # Legs
    Legs = Line(Point(300, 395), Point(310, 420))
    Legs.setFill('black')
    Legs1 = Line(Point(300, 395), Point(290, 420))
    Legs1.setFill('black')
    Arms = Line(Point(300, 345), Point(270, 370))
    Arms.setFill('black')

    bat2 = Oval(Point(210, 365), Point(285, 373))
    bat2.setFill(color_rgb(210, 129, 67))
    bat = Oval(Point(270,300), Point(275,373))
    bat.setFill(color_rgb(210, 129, 67))

    if(globals()['batting']):
        globals()['bat2drawing'] = True
        bat.move(800,800)
        bat2.draw(Window)

    else:
        if(globals()['bat2drawing']):
            bat2.undraw()
            bat.move(-800,-800)

    bat.draw(Window)
    Arms.draw(Window)
    Legs1.draw(Window)
    Legs.draw(Window)
    Body.draw(Window)
    Head.draw(Window)







def BatterUP(window):


    if(globals()['pitching']):

        if(window.getKey() == "space"):

            globals()['batting'] = True
        else:
            globals()['batting'] = False



#different Pitches

def generatePitch():

    return ran.uniform(0.03,0.06)

def generateCurve():

    return ran.uniform(-0.001,-0.0065)

main()