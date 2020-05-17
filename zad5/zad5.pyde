class Plane(object):
    def __init__(self, c, xpos, ypos, xspeed):
        self.c = c
        self.xpos = xpos
        self.ypos = ypos
        self.xspeed = xspeed
        
    def display(self):
        stroke(0)
        fill(self.c)
        rectMode(CENTER)
        rect(self.xpos, self.ypos, 30, 20)
        
    def fly(self):
        self.xspeed = 1
        self.xpos += self.xpos + self.xspeed;
        if self.xpos > width:
            self.xpos = 0
            print(x)
x = 0
 
 
def setup():
    size(200,200)
    global planes
    Plane1 = Plane(color(0,0,255),0,100,2)
    Plane2 = Plane(color(255,0,0),0,50,1)
    Plane3 = Plane(color(0,255,0),0, 150, 3)
    planes= (Plane1, Plane2, Plane3)
def draw():
    global x
    background(255)
    for plane in planes: # przy trzech już chyba warto spiąć w kolekcję ;)
        plane.fly()
        plane.display()
    x += 1
    print(x)
    if mousePressed:
        exit()
        
# 2 pkt, o to chodziło
