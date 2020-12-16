

with open('q11.txt') as f:
    # 2d array
    J = list(map(lambda x: list(x), f.read().split()))
    

lenX = len(J[0])
lenY = len(J)




def inMap(x,y):
    return (0 <= x < lenX) and (0 <= y < lenY)



steps = [
 [1,0], [0,1], [1,1], [-1,1]   
]

buf = []
for step_x, step_y in steps:
    buf.append([step_x*-1, step_y*-1])
    
steps += buf


def walk(x,y, sX, sY):
    '''
    Walks a path along a diagonal, and gets the first
    item that is visible (path defined by Sx,sY).
    '''
    x += sX
    y += sY
    while inMap(x,y):
        if J[x][y] != '.':
            return J[x][y]
        x += sX
        y += sY        
    return '.'


def neighbours(X, Y):
    neighbours = []
    """
    # # #
    # # # <- middle = (x,y)
    # # #
    """
    for sX, sY in steps:
        neighbours.append(walk(X,Y, sX, sY))
    return neighbours


rules = {
  'L' : lambda x,y : '#' if neighbours(x,y).count("#") == 0 else 'L',
  '#' : lambda x,y : 'L' if neighbours(x,y).count('#') >= 5 else '#',
  '.' : lambda x,y : '.'
}



def prettyPrint(L):
    for u in L:
        print(''.join(u))


def eq(L,J):
    if J is None:
        return False
    
    for i in range(len(L)):
        if L[i] != J[i]:
            return False
    return True


def step(L):
    new = []
    for i in range(lenY):
        new.append([None] * lenX)
        
    assert len(new) == len(J), 'len not eq'
    assert len(new[0]) == len(J[0]), 'len not eq'
    
    for x,e1 in enumerate(L):
        for y,e2 in enumerate(e1):
            new[x][y] = rules[e2](x,y)
            
    return new


lst = None



while not eq(J,lst):
    lst = J
    J = step(J)

cnt = 0
for e in J:
    cnt += e.count("#")

print(cnt)