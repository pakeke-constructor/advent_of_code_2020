




with open('q10.txt') as f:
    J = list(map(lambda x:int(x), f.read().split()))

J.sort()
J.insert(0, 0)
J.append(J[-1]+3)

diffs = []


for i,e in enumerate(J):
    if i!=0:#skip first    
        assert e > J[i-1], "err!"
        diffs.append(e-J[i-1])



oGroups = []

st = -1


for i,e in enumerate(diffs):
    if e==1:
        if st==-1:
            st = i
    else: # e is 3.
        if st != -1:
            oGroups.append((st,i-1))
        st=-1

d = {
 # hardcoded in- yes, bad, but couldn't find an actual solution!
 1 : 1,
 2 : 2,
 3 : 4,
 4 : 7
}

u=1

for s,f in oGroups:
    if (f-s)+1:
        u *= d[(f-s)+1]
    
print(u)