# Print todo.txt
def listpm(todo_path):
    cnt = 1
    f= open(todo_path+'todo.txt','r')
    for line in f:
        if line[0] != "x":
            print(str(cnt)+" "+line[:-1])
        cnt = cnt + 1
        
    f.close()
