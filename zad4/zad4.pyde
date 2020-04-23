add_library('pdf')
import random

        



def setup():
    global img
    global oku
    global oku2
    size(400,400)
    img = loadImage("foto.png")
    oku = loadImage("oku.png")
    oku2 = loadImage("oku2.png")
    beginRecord(PDF,"outfoto.pdf")
    
    print(random.random())
    print(type(img))
    image(img,100,70)#zdjęcie
    
def draw():
    print(mouseX,mouseY)
    global img
    global oku
    global oku2
    
    if keyPressed:
        if key == CODED:
            if keyCode == RIGHT:
                image(oku,141,180,120,45)
    if keyPressed:       
        if key == CODED:
            if keyCode == LEFT:
                image(oku2,140,180,120,50)
    
    #image(oku,141,180,120,45)#1 para
    #image(oku2,140,180,120,50)#2 para
    
    
def mousePressed():
    endRecord()
    exit()
