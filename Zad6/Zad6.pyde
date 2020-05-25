class Kwadrat():
    def __init__(self, bok): 
        self.bok = bok
    def sketch(self, x, y):
        self.x = x
        self.y = y
        rect(self.x, self.y, self.bok, self.bok)
        
class PasiastyKwadrat(Kwadrat):
    def sketchPasiasty(self, x, y, paski): 
        Kwadrat.sketch(self, x, y)
        space = self.bok/paski
        _xLinii_ = 0 
        for pasek in range(0, paski): 
            line(x+_xLinii_, y, x+_xLinii_, y+self.bok)
            _xLinii_ +=space
            
class KwadratKolor(Kwadrat):
    def sketchKolor(self, x, y, r, g, b):
        fill(r,g,b)
        Kwadrat.sketch(self, x, y)
        
def setup():
    size(500, 500)
    
    Blu = KwadratKolor(50)
    Blu.sketchKolor(0, 0, 0, 0, 255)
    Red = KwadratKolor(50)
    Red.sketchKolor(450,450,255,0,0)
