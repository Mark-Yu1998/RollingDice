from graphics import *
from random import *

width = 140
height = 150
space = 15
currentText = Text(Point(100,230),"0")

def exitButton(win):
    exitBtn = Rectangle(Point(910,250),Point(990,290))
    exitBtn.setFill("Yellow")
    exitBtn.draw(win)
    Exit = Text(Point(950,270),"Exit")
    Exit.setFill("Blue")
    Exit.setSize(20)
    Exit.draw(win)
def drawBox(win):
    topLeft = []
    btmRight = []
    
    current = Point(10,10)
    
    for i in range (6):
        #coordinates of top left corners of the box
        topLeft.append(current)

        #coordinates of the bottom right corners of the box
        goto = Point(current.getX() + width,height)

        #Drawing the dots
        left = Circle(current,5)
        right = Circle(goto,5)
        left.setFill("Green")
        right.setFill("Yellow")
        left.draw(win)
        right.draw(win)
        
        btmRight.append(goto)

        """draw the boxes"""
        rect = Rectangle(current,goto)
        rect.setOutline("White")
        rect.draw(win)
        current = Point(current.getX() + width + space,10)
        
    return topLeft,btmRight

def getCenter(topLeft,btmRight):
    centers = []
    for i in range (len(topLeft)):
        centerX = (btmRight[i].getX() - topLeft[i].getX()) // 2
        centerY = (btmRight[i].getY() - topLeft[i].getY()) // 2 + 10
        centers.append(Point(topLeft[i].getX() + centerX,centerY))
    return centers

def drawDots(win,center):
    nDots = randint(1,6)
##    print("{0} dots".format(nDots))
    dot1 = Circle(Point(0,0),0)
    dot2 = Circle(Point(0,0),0)
    dot3 = Circle(Point(0,0),0)
    dot4 = Circle(Point(0,0),0)
    dot5 = Circle(Point(0,0),0)
    dot6 = Circle(Point(0,0),0)
    # Draw dots base on the random number
    if nDots == 1:
        dot1 = Circle(center,15).draw(win)
        dot1.setFill("White")
    elif nDots == 2:
        dot1 = Circle(Point(center.getX() - width // 4,center.getY() + height // 4),15).draw(win)
        dot2 = Circle(Point(center.getX() + width // 4,center.getY() - height // 4),15).draw(win)
        dot1.setFill("White")
        dot2.setFill("White")
    elif nDots == 3:
        dot1 = Circle(center,15).draw(win)
        dot1.setFill("White")
        dot2 = Circle(Point(center.getX() - width // 4,center.getY() + height // 4),15).draw(win)
        dot2.setFill("White")
        dot3 = Circle(Point(center.getX() + width // 4,center.getY() - height // 4),15).draw(win)
        dot3.setFill("White")
    elif nDots == 4:
        dot1 = Circle(Point(center.getX() - width // 4,center.getY() + height // 4),15).draw(win)
        dot2 = Circle(Point(center.getX() + width // 4,center.getY() - height // 4),15).draw(win)
        dot3 = Circle(Point(center.getX() - width // 4,center.getY() - height // 4),15).draw(win)
        dot4 = Circle(Point(center.getX() + width // 4,center.getY() + height // 4),15).draw(win)
        dot1.setFill("white")
        dot2.setFill("white")
        dot3.setFill("white")
        dot4.setFill("white")
    elif nDots == 5:
        dot1 = Circle(center,15).draw(win)
        dot2 = Circle(Point(center.getX() - width // 4,center.getY() + height // 4),15).draw(win)
        dot3 = Circle(Point(center.getX() + width // 4,center.getY() - height // 4),15).draw(win)
        dot4 = Circle(Point(center.getX() - width // 4,center.getY() - height // 4),15).draw(win)
        dot5 = Circle(Point(center.getX() + width // 4,center.getY() + height // 4),15).draw(win)
        dot1.setFill("White")
        dot2.setFill("white")
        dot3.setFill("white")
        dot4.setFill("white")
        dot5.setFill("white")
    elif nDots == 6:
        dot1 = Circle(Point(center.getX() - width // 4,center.getY() + height // 4),15).draw(win)
        dot2 = Circle(Point(center.getX() + width // 4,center.getY() - height // 4),15).draw(win)
        dot3 = Circle(Point(center.getX() - width // 4,center.getY() - height // 4),15).draw(win)
        dot4 = Circle(Point(center.getX() + width // 4,center.getY() + height // 4),15).draw(win)
        dot5 = Circle(Point(center.getX() - width // 4,center.getY()),15).draw(win)
        dot6 = Circle(Point(center.getX() + width // 4,center.getY()),15).draw(win)
        dot1.setFill("white")
        dot2.setFill("white")
        dot3.setFill("white")
        dot4.setFill("white")
        dot5.setFill("white")
        dot6.setFill("white")
    return nDots

def compute_display(win,currentSum):
    label = Text(Point(100,200),"current sum:").draw(win)
    label.setSize(20)
    currentText.setText(currentSum)
    label.setFill("White")
    currentText.setSize(20)
    currentText.setFill("white") 
def main():
    win = GraphWin("Rolling dice",1000,300)
    win.setBackground("black")
    exitButton(win)
    drawBox(win)
    #Top left coordinates and buttom right coordinates
    tCoord = drawBox(win)[0]
    bCoord = drawBox(win)[1]
    center = getCenter(tCoord,bCoord)
    canRun = True
    currentSum = 0
    dots = 0
    currentText.draw(win)
    msg = Text(Point(500,250),"")
    while (canRun):
        compute_display(win,currentSum)
        loca = win.getMouse()
        xCoord = loca.getX()
        yCoord = loca.getY()
        
        for current in center :
            if xCoord >= current.getX() - width // 2 and xCoord <= current.getX() + width // 2 and yCoord >= current.getY() - height // 2 and yCoord <= current.getY() + height // 2:
                dots = drawDots(win,current)
                center.remove(current)
                currentSum += dots
 
        if xCoord >= 910 and xCoord <= 990 and yCoord >= 250 and yCoord <= 290:
            win.close()
            canRun = False
            
        elif len(center) == 0:
            if (currentSum > 15):
                msg.setText("You won!!!")
                msg.setFill("Yellow")
                msg.draw(win)
            else:
                msg.setText("You lose sucka!!")
                msg.setFill("red")
                msg.draw(win)       
main()
