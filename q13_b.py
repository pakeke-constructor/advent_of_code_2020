


with open('q13.txt') as f:
    u = f.read().split()
    _ = int(u[0])
    buses = u[1].split(",")
    

time = 0


def found(i, t1, t2):
    n1, pos1 = t1
    n2, pos2 = t2
    return ((i + pos1) % n1 == 0) and ((i + pos2) % n2 == 0)
        


def correllate(t1, t2):
    '''
    returns  repeating factor (n), start position (i)
    '''
    n1, pos1 = t1
    n2, pos2 = t2
    
    if n1 == 'x' and n2 == 'x':
        raise ValueError('vdfdf')
    
    if n1 == "x":
        return t2
    elif n2 == 'x':
        return t1
    
    n2 = int(n2)
    n1 = int(n1)
    t1 = (n1, pos1)
    t2 = (n2, pos2)
    
    if n1 > n2:# use steps of n1.
        d = pos1 - pos2
        i = -pos1        
        while not found(i, t1, t2):
            i += n1
    else:
        # n2 > n1. use steps of n2.
        d = pos2 - pos1
        i = -pos2        
        while not found(i, t1, t2):
            i += n2    

    return (n1*n2), -i


from functools import reduce


print(
    -reduce(correllate, zip(buses, range(len(buses))))[-1]
)

