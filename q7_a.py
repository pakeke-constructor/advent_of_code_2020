

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
            ar.append(''.join(filter(u, e)).strip())
        d[k] = ar
    return d



def contains(rule, bag, search)-> bool:
    if bag == search:
        return True
    
    for b in rule[bag]:
        if contains(rule, b, search):
            return True
    return False


@ee
def solve(inp):
    rule = make_rules(inp)
    ct = 0
    with open('testfile.txt', "w") as f:
        for bag,_ in rule.items():
            s = bag + "=" + ':'.join(_) + "\n"
            f.write(s)
            ct+=contains(rule, bag, 'shiny gold')
    return ct


solve(main)