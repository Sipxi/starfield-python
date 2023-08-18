import random

def map_range(value: float, start1: float, stop1: float, start2: float, stop2: float) -> float:
   return (value - start1) / (stop1 - start1) * (stop2 - start2) + stop2
colors = [ "red", "yellow", "orange", "white" ]
width = 800 /2
height = 600 /2

class Star:
    def __init__(self) -> None:
        self.color = random.choice(colors)
        self.x = random.randint(-width, width)
        self.y = random.randint(-height, height)
        self.z = random.randint(0, width)
        self.x
        self.pz = self.z
    
    def show(self, canvas) -> None:
        sx = map_range(self.x/self.z, 0 ,1, 0, width)
        sy = map_range(self.y/self.z, 0 ,1, 0, height)
        
        radius = map_range(self.z, width, 0, 8, 0)
        
        px = map_range(self.x/self.pz, 0 ,1, 1, width)
        py = map_range(self.y/self.pz, 0 ,1, 1, height)
        
        self.pz = self.z
        
        canvas.create_line(px, py, sx+ (radius/2), sy + (radius/2), fill=self.color, tags = "delete", width=abs(abs(radius)-2))
        canvas.create_oval(sx , sy , sx+ radius , sy+ radius, fill = self.color , outline=self.color, tags = "delete")

    
    def update(self, canvas, speed) -> None:
        self.z = self.z - speed
        if (self.z < 1 or self.z > 600):
            self.z = width
            self.x = random.randint(-width, width)
            self.y = random.randint(-height, height)
            self.pz = self.z
        self.show(canvas)
        
    
    