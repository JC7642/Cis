def setup():
    size(600, 600)
    textSize(80)

def draw():
    print(pmouseX,pmouseY)
    clear()
    if keyPressed:
        if (key == CODED):
            if (keyCode == 37):
                fill(0, 255, 0, 255)
        if (key == CODED):
            if (keyCode == 39):
                fill(255, 255, 255, 255)
    if keyPressed:
        if (key == 'c'):
            fill(255, 255, 255, 255)
    elif (mouseX >= 194) and (mouseX <= 218) and (mouseY >= 243) and (mouseY <= 299):
        fill(0, 255, 0, 255)
    else:
        fill(255,255,255,255)
    
    text("J", 200, 300)
    
    
    if keyPressed:
        if (key == CODED):
            if (keyCode == 39):
                fill(0, 255, 0, 255)
            if (keyCode == 37):
                fill(255, 255, 255, 255)
        if (key == 'c'):
            fill(0, 255, 0, 255)
    else:
        fill(255,255,255,255)
        
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
