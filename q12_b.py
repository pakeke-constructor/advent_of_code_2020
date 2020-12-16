
from math import sin,cos,radians,atan2,pi

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


dist = lambda x,y : (x**2 + y**2)**0.5


rots= {
  0  : lambda x,y : [0,0],
  90 : lambda x,y : [-y, x],
  180 : lambda x,y :[-x, -y],
  270 : lambda x,y : [y, -x],
  -90 : lambda x,y : [y, -x],
  -180 :lambda x,y :[-x, -y],
  -270 : lambda x,y : [-y, x]
}

class WPShip(Ship):
    def __init__(s, parent):
        super().__init__()
        s.parent = parent
        s.wp = [10,1]
        s.r = (atan2(1,10)/pi)*180
    
    def move(s,x,y):
        s.wp[0]+=x
        s.wp[1]+=y
    
    def rot(s,deg):
        s.wp = rots[deg%360](*s.wp)
        s.r += deg
        s.r=round(s.r)
        
    def forward(s, units):
        s.parent.move(units*s.wp[0], units*s.wp[1])
        
    def getDist(s):
        return s.parent.getDist()



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
wp = WPShip(S)


for e in u:
    cmd = e[0]
    arg = int(e[1:])
    print(wp.wp[0], wp.wp[1])
    move[cmd](wp, arg)

print(wp.getDist())
