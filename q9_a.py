



with open("q9.txt") as f:
    IN = f.read().split()
    
    u=0
    for each in IN:
        IN[u] = int(each)
        u+=1

LEN = 25


for i in range(LEN,len(IN)):
    nums = IN[i-LEN:i]
    
    isValid = False
    for i1, n1 in enumerate(nums):
        for i2, n2 in enumerate(nums):
            if i2 != i1:
                if n2 + n1 == IN[i]:
                    isValid = True
    
    if not isValid:
        print(IN[i])
        break
    



