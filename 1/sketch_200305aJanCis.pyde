def setup():
    size(400,600)
    rectMode(CORNER)

def draw():
    print(mouseX,mouseY,mousePressed)
    if mousePressed:
         rect(width/2,height/2,300,500)
         line(50,200,60,220)
    else:circle(30,30,40)
        
