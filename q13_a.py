

with open('q13.txt') as f:
    u = f.read().split()
    time = int(u[0])
    buses = u[1].split(",")
    
    
    
def noRide(i):
    'if there is no ride at time `i`, returns true.'
    for each in buses:
        if each != "x":
            if i % int(each) == 0:
                return False, each
    return True, None
    
    
i = time
noR, bus = noRide(i)

while noR:
    i += 1
    noR, bus = noRide(i)

print(i-time, bus)    

