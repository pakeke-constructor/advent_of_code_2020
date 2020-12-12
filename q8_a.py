






with open('q8_a.txt',"r") as f:
    main = f.read()


def ee(f):
    def modded(*a,**k):
        g = f(*a,**k)
        print(g)
        return g
    return modded



class Ins:
    pass
I=Ins()

I.val = 0
I.i = 0
I.commands = []



def jmp(I,a):
    I.i += a

def acc(I,a):
    I.val += a
    jmp(I,1)


# Each cmd takes func: function( I, arg : int ) : None 
CMDS={
    "nop" : lambda II, y: jmp(II, 1),
    "jmp" : jmp,
    "acc" : acc
}


def run(cmd)-> bool:
    'returns True if program should stop running'
    if cmd[2]:
        return True
    CMDS[cmd[0]](I, cmd[1])
    cmd[2] = True
    return False



def paz(inp):
    for command in inp.split("\n"):
        if not command: continue
        
        cmd_t, arg = command.split(" ")
        arg = int(arg)
        
        # [ cmd_type, argument, has_ran ]
        I.commands.append([cmd_t, arg, False])

def step():
    cmd = I.commands[I.i]
    return run(cmd)

@ee
def solve(inp):
    paz(inp)
    while (not step()): pass
    
    return I.val


solve(main)




