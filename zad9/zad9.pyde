def setup():
    global img
    size(500,500)
    img = loadImage("plik.jpg")
    
    
def draw():
    global img
    try:
        rect(144,143,210,210)
        stroke(0,0,255)
        image(img, 150,150)
        img.resize(200,200)
    
    except:
        text("Brak pliku", 400,450)
        stroke(255,0,0)
        
        
