import sys
import time
import subprocess

from pydoro import work_time, break_short, break_long, audio_file
import pomo


# Start pomodoro timer
def pomodoro(todo_path,todo_linenmbr):
    global work_time, break_short, break_long, audio_file

    f = open(todo_path+'/todo.txt','r')
    todo = f.readlines()[int(todo_linenmbr)-1]
    f.close()

    if todo[0] == "x":
        print("pydoro: unvalid todo number")
        exit(-1)

    print("pydoro: started pomodoro timer.")

    cnt = 1
    while True:
        if cnt % 2 == 1:
            t = pomo.increment(todo_path, todo_linenmbr)
            print("Working on: " + t[:-1])
                
            # Write to logfile
            log = time.asctime()+" - started todo: "+todo[:-1]+"\n"
            with open(todo_path+'/pydoro.log','a+') as logfile:
                logfile.write(log)

            # Play notification
            subprocess.call(["afplay",audio_file])

            # Start timer
            pomo.timer(work_time)

            # Play notification
            subprocess.call(["afplay",audio_file])

            # Write to logfile
            log = time.asctime()+" - stopped todo: "+todo[:-1]+"\n"
            with open(todo_path+'/pydoro.log','a+') as logfile:
                logfile.write(log)

        elif cnt % 2 == 0:
            print("pydoro: Pomodoro finished.\n\t- 'b' to take break\n\t- 's' to skip break\n\t- 'q' to quit pydoro")
            answr = input("")
            if answr == "s":
                print("Skipping break..")
            elif answr == "b":
                if cnt == 8:
                    print("Taking long break: "+str(break_long)+" minutes..")
                    pomo.timer(break_long)
                else:
                    print("Taking short break: "+str(break_short)+" minutes..")
                    pomo.timer(break_short)
                print("pydoro: Break finished.")
                answr = input("You want to continue with pomodoros [y/n]: ")
                if answr not in ['y','Y','YES','yes']:
                    print("pydoro: Exiting...")
                    exit(-1)
            elif answr == "q":
                print("Done with pomodoros. Exiting..")
                exit(-1)
            else:
                print("Invalid option..")
                exit(-1)

        if cnt == 8:
            cnt = 1
        else:
            cnt = cnt + 1

