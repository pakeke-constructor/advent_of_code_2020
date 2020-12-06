


def ee(f):
    def modded(*a,**k):
        g = f(*a,**k)
        print(g)
        return g
    return modded


MAIN_SET = set(main)


def ct(st):
    ss = set(MAIN_SET)
    for val in st.split():
        this = set()
        for char in val:
            this.add(char)
        ss = ss.intersection(this)
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
    

