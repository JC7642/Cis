def setup():
    size(600, 600)
    textSize(80)
    global bialy
    bialy = (255, 255, 255, 255) # czasem warto stworzyć zmienną dla powtarzającego się elementu tak po prostu dlaczytelności

def draw():
    print(pmouseX,pmouseY)
    clear()
    if keyPressed:
        if (key == CODED):
            if (keyCode == 37):
                fill(0, 255, 0, 255)
        if (key == CODED):
            if (keyCode == 39):
                fill(*bialy)
        if (key == 'c'):
            fill(*bialy)
    elif (mouseX >= 194) and (mouseX <= 218) and (mouseY >= 243) and (mouseY <= 299):
        fill(0, 255, 0, 255)
    else:
        fill(*bialy)
    
    text("J", 200, 300)
    
    
    if keyPressed:
        if (key == CODED):
            if (keyCode == 39):
                fill(0, 255, 0, 255)
            if (keyCode == 37):
                fill(*bialy)
        if (key == 'c'):
            fill(0, 255, 0, 255)
    else:
        fill(*bialy)
        
    text("C", 300, 300)
    
    
    s = createShape()
    s.beginShape()
    s.fill(165, 0, 249, 255)
    s.stroke(165, 0, 249, 255)
    s.vertex(200, 350)
    s.vertex(250, 450)
    s.vertex(475, 420)
    s.vertex(363, 380)
    s.endShape(CLOSE)
    shape(s, 10, 10)
    
    # całkiem ładnie, jedyny mankament, że same stzałki bez zaznaczenia litery też działają; ale to było troszkę tricky
    # więc uznaję: 2pkt
