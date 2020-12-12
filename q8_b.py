



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



def done(I,a):
    I.isSolution = True
    I.done = True
    


def jmp(I,a):
    I.i += a

def acc(I,a):
    I.val += a
    jmp(I,1)
    
def wrongDone(I,a):
    I.isSolution = False
    I.done=True



# Each cmd takes func: function( I, arg : int ) : None 
CMDS={
    'wrongDone' : wrongDone,
    'done': done,
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
    I.val = 0
    I.i = 0
    I.commands = []
    I.isSolution=False
    
    for command in inp.split("\n"):
        if not command: continue
        
        cmd_t, arg = command.split(" ")
        arg = int(arg)
        
        # [ cmd_type, argument, has_ran ]
        I.commands.append([cmd_t, arg, False])
        
    I.commands.append(['done', 0, False])
    
    for i in range(500):
        I.commands.append(['wrongDone',0,False])
        
    mutable_indexes = []
    for i, (cmd_t, arg, hasRan) in enumerate(I.commands):
        if cmd_t == "jmp" or cmd_t == "jmp":
            mutable_indexes.append(i)

    return mutable_indexes




def step():
    cmd = I.commands[I.i]
    return run(cmd)


inverse = lambda x: [('jmp' if x[0] == 'nop' else 'nop'), x[1], x[2]]




def solve(inp):
    idx = paz(inp)
    
    for i in idx:
        I.commands[i] = inverse(I.commands[i])
        while (not step()):
            pass
        
        if I.isSolution:
            print(I.val)
            
        paz(inp)
    
    return I.val


solve(main)


