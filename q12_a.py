
from math import sin,cos,radians

class Ship:
    def __init__(s):
        s.x = 0
        s.y = 0
        s.r = 0
        
    def move(s,x,y):
        s.x += x
        s.y += y
        
    def rot(self, deg):
        self.r += deg
        self.r = round(self.r)
        
    def forward(s, n):
        s.x += cos(radians(s.r))*n
        s.y += sin(radians(s.r))*n
    
    def getDist(s):
        return abs(round(s.x)) + abs(round(s.y))


move={
   'N' : lambda S, arg : S.move(0, arg),
   'S' : lambda S, arg : S.move(0, -arg),
   'E' : lambda S, arg : S.move(arg, 0),
   'W' : lambda S, arg : S.move(-arg, 0),
   'L' : lambda S, arg : S.rot(arg),
   'R' : lambda S, arg : S.rot(-arg),
   'F' : lambda S, arg : S.forward(arg)
}


with open('q12.txt') as f:
    u = f.read().split()
    
    
    
    
S = Ship()    

for e in u:
    cmd = e[0]
    arg = int(e[1:])
    move[cmd](S, arg)


print(S.getDist())
