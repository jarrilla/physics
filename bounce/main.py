# Simulate a bouncing ball
# influenced by simple gravity g=9.8 m/s^s
# and lack of air resistance.

from graphics import *

# constants
g = 9.8 # m/s^2
dt = 0.0015 # seconds

# initial configuration
y0 = 575 # max height - 25
x0 = 400 # middle of screen
y_min = 100 # ground level (-500)
v0 = 0
ballRadius = 20

# graphics globals
win = GraphWin("bounce", 800, 600, autoflush=False)
win.setCoords(0, 0, 800, 600) # set coordinates to be "physical"
ball = Circle( Point(x0, y0) , ballRadius)
ground = Line( Point(0, y_min), Point(800, y_min) )

def initGraphics():
  ball.setFill("red")
  ball.setOutline("red")
  ball.draw(win)

  ground.draw(win)
  win.getMouse()

def sim():
  a = -g
  
  y = y0
  v = v0

  while True:
    # bounce when ball hits ground
    if (y <= y_min + ballRadius):
      v = -v
    
    # update position and velocity
    dv = a * dt
    v = v + dv
    dy = v * dt
    y = y + dy

    # move ball
    ball.move(0, dy)
    update()

def main():
  initGraphics()
  sim()

main()