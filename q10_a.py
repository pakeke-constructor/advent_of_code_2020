




with open('q10.txt') as f:
    J = list(map(lambda x:int(x), f.read().split()))

J.sort()
diffs = []
J.insert(0, 0)
J.append(J[-1]+3)


for i,e in enumerate(J):
    if i!=0:#skip first
        assert e > J[i-1], "err!"
        diffs.append(e-J[i-1])


print("3s : ", diffs.count(3))
print("1s : ", diffs.count(1))

    

