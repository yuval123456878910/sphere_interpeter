import sys, sphere
commands = sys.argv

def get_all(list_c: list, locations: list):
    list_n = []
    current_item = None
    for token in list_c:
        current_item = token
        for location in locations:
            current_item = current_item[location]
        list_n.append(current_item)
    return list_n

code = []
if len(commands) >= 2:
    with open(commands[1], "r") as file:
        code = file.readlines()

    st = {} # storege
    if_1 = [None] # if state (list if "if" is true, false or need to stop)
    for i in code:
        run = sphere.tokenizer(i)     
        run = sphere.parser(run)
        if 2 <= len(if_1):
            if if_1[-1] == "true" or 'elif' in get_all(run, [1,1]) or 'else' in get_all(run, [1,1]) or 'endif' in get_all(run, [1,1]) or 'if' in get_all(run, [1,1]):
                run, if_1 = sphere.finalise(run, st, if_1)     
                run = sphere.veruble_config(run, st)
                
        else:
            run, if_1 = sphere.finalise(run, st, if_1)            
            run = sphere.veruble_config(run, st)
