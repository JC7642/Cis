def setup():
    size(500,500)
    frameRate(20)
    global x, y
    x = 0
    y = height/2
    global xspeed
    global yspeed
    xspeed = 10
    yspeed = 10 
    global slownik_kolorow
    slownik_kolorow = {"czerwony":(255,0,0, 80), "niebieski":(0,0,255,80), "zielony":(0,255,0,80)} # mógłbyś chociaż zmienić kolory, nie kusiło Cię to? ;)
    global lista_kolorow
    lista_kolorow = []
    
    for klucz, wartosc in slownik_kolorow.items():
        lista_kolorow.append(wartosc)
    global iteracja_programu
    iteracja_programu = 0
    
def draw():
    global x
    global y
    global xspeed
    global yspeed
    global iteracja_programu
    
    iteracja_programu +=1
    stroke(*slownik_kolorow["czerwony"])
    fill(*lista_kolorow[iteracja_programu%len(lista_kolorow)])
    rectMode(CENTER)
    
    x += xspeed
    if (x > width or x < 0):
        xspeed *=-1;
        
    y += yspeed
    if (y > height or y < 0):
        yspeed *=-1
    rect(x, y, 70, 70)
    
    if mousePressed:
        exit()
        
# 2pkt
