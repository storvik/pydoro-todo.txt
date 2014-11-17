import re
import string

def increment(todo_path, todo_linenmbr):
    with open(todo_path+'/todo.txt', 'r') as file:
        todo_file = file.readlines()

    if int(todo_linenmbr) > len(todo_file):
        print("pydoro: Invalid todo number..")
        exit(-1)
        
    t = todo_file[int(todo_linenmbr)-1]
    regex = re.compile("\(#pomo [0-9]*\)")

    # If no previous pomodoros
    todo_pomo = regex.findall(t)
    if len(todo_pomo) == 0:
        t = t[:-1] + " (#pomo 1)\n"
    else:
        regex = re.compile("[0-9]+")
        pomo_numbr = regex.findall(todo_pomo[0])

        t = t[:-1-len(todo_pomo[0])-1] + " (#pomo " + str(int(pomo_numbr[0])+1) + ")\n"
                
    todo_file[int(todo_linenmbr)-1] = t
            
    # Write new todo.txt
    with open(todo_path+'/todo.txt', 'w') as file:
        file.writelines(todo_file)

    return t
