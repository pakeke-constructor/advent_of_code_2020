



def ee(f):
    def modded(*a,**k):
        g = f(*a,**k)
        print(g)
        return g
    return modded



def ct(st):
    ss = set()
    for val in st.split():
        for char in val:
            ss.add(char)
    if "\n" in ss:
        ss.remove("\n")
    if " " in ss:
        ss.remove(" ")

    return len(ss)

@ee
def solve(inp):
    am = 0
    for s in inp.split("\n\n"):
        am += ct(s)
    return am
    

