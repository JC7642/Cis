def setup():
    global img
    size(500,500)
    img = loadImage("plik.jpg")
    noFill()
    
def draw():
    global img
    try:        
        image(img, 150,150) # tylko to wystarczy sprawdzać
    
    except:
        text("Brak pliku", 400,450)
        stroke(255,0,0)
    else:
        img.resize(200,200)
        stroke(0,0,255)
    finally:
        rect(144,143,210,210)

# 1,5pkt
