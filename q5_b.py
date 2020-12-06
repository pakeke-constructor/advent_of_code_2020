





def ee(f):
    def modded(*a,**k):
        g = f(*a,**k)
        print(g)
        return g
    return modded



ROW = 2**7

SEATS = 2**3


def getRowAndSeat(str) -> (int,int):

    row = 0    
    curR = ROW//2

    seat = 0
    curS = SEATS//2

    for i in range(7):
        r = str[i]
        if r == 'F':
            # take lower:
            pass # (already at lower)
        else:
            assert r=='B', r
            # take upper.
            row += curR
        curR//=2
    
    for i in range(3):
        r = str[7+i]
        if r == 'L':
            # take lower:
            pass # (already at lower)
        else:
            assert r=='R', r
            # take upper.
            seat+= curS

        curS//=2

    return (row, seat)




@ee
def solve(inp):
    ar=[]
    for e in inp.split():
        ar.append( getRowAndSeat(e) )

    while '' in ar:
        ar.remove('')
    
    ar = list(map((lambda x : ((x[0]*8 + x[1]), x) ), ar))
    ar.sort(key = lambda x : x[0])
    
    lst = None
    for i,e in enumerate(ar):
        if lst is not None:
            if abs(lst[0] - e[0]) > 1:
                return lst[0] + 1
        lst = e
        



solve(main)




