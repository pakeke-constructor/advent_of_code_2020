

def ee(f):
    def modded(*a,**k):
        g = f(*a,**k)
        print(g)
        return g
    return modded


DIGITS = set('0123456789')

f = lambda X:X.replace("bags,","").replace("bag,","").replace("bags.","").replace("bag.","").replace(" bags ","").replace(" bag ","").strip()



def make_rules(inp):
    u = lambda ii : not(ii in DIGITS)
    not_u = lambda ii : (ii in DIGITS)
    d={}
    for s in inp.split("\n"):
        if not s: continue
        st, fi = s.split("contain ")
        k = f(st)
        if 'no other bags' in fi:
            d[k] = []
            continue
        ar = []
        for e in fi.split(","):
            # void de numbers
            e=f(e + " ")
            amt = int(''.join(filter(not_u, e)).strip())
            col = (''.join(filter(u, e)).strip())
            ar.append((amt, col))
        d[k] = ar
    return d



def contains(rule, bag, search)-> bool:
    if bag == search:
        return True
    
    for b in rule[bag]:
        if contains(rule, b, search):
            return True
    return False


def count(rule, bag):
    ct = 1
    for am, bg in rule[bag]:
        ct += am*count(rule, bg)
    return ct



@ee
def solve(inp):
    rule = make_rules(inp)
    for k,v in rule.items():
        print(k,v)
    ct = count(rule, "shiny gold")
    return ct



