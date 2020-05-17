add_library('pdf')
import random

def setup():
    global img
    global oku
    global oku2
    size(400,400) # to nie jest proporcja zdjęcia dokumentowego
    img = loadImage("foto.png")
    oku = loadImage("oku.png")
    oku2 = loadImage("oku2.png")
    
    print(random.random())
    print(type(img))
    beginRecord(PDF,"outfoto.pdf")
    
def draw():
    
    print(mouseX,mouseY)
    global img
    global oku
    global oku2
    image(img,100,70)#zdjęcie
    if key == "1":
        image(oku,141,180,120,45)
    elif key == "2":      
        image(oku2,140,180,120,50)
    
    #image(oku,141,180,120,45)#1 para
    #image(oku2,140,180,120,50)#2 para
    
    
def mousePressed():
    endRecord() # to sprawi, że nagra się tyle warst plików ile klatek się wykona zanim się kliknie
    exit()
    
# 1,75pkt
