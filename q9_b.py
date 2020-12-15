



with open("q9.txt") as f:
    IN = f.read().split()
    
    u=0
    for each in IN:
        IN[u] = int(each)
        u+=1

LEN = 25


badIndex = None
badNum   = None


for i in range(LEN,len(IN)):
    nums = IN[i-LEN:i]
    
    isValid = False
    for i1, n1 in enumerate(nums):
        for i2, n2 in enumerate(nums):
            if i2 != i1:
                if n2 + n1 == IN[i]:
                    isValid = True
    
    if not isValid:
        badIndex = i
        badNum   = IN[i]
        break



def sumTo(IN,j,bad):
    ar=[]
    for i in range(j,len(IN)):
        if sum(ar) == bad:
            return True, ar
        elif sum(ar) > bad:
            return False, ar
        ar.append(IN[i])
    return False, ar


for j in range(len(IN)):
    sumsToNum, ar = sumTo(IN,j,badNum)
    if sumsToNum: 
        print("array (debug)", ar)
        print("sum", sum(ar))
        print("max(ar) + min(ar)", min(ar) + max(ar))
        break








