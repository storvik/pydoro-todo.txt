#!/usr/local/bin/python3

import os
import sys

import pomo

work_time = 25
break_short = 5
break_long = 20
audio_file = os.path.realpath(__file__)[:-9] + "pomo.wav"

def print_help():
    print("pydoro todo.txt-cli plugin by Storvik")
    print("Usage:\ttodo.txt pd [arguments]")
    print("\t- help       \t- Write help information")
    print("\t- ls         \t- List todos")
    print("\t- start 'nmb'\t- Start pomodoro on todo")
    print("\t- increment  \t- Increment pomodoro on todo")
    print("\t- decrement  \t- Decrement pomodoro on todo")
    print("")
    
if __name__ == '__main__':

    todo_path = os.environ.get('TODO_DIR')

    if len(sys.argv) < 3:
        print("pydoro: Wrong input...")
        exit(-1)

    if sys.argv[2] == "help":
        print_help()
    elif sys.argv[2] == "ls":
        pomo.listpm(todo_path)
    elif sys.argv[2] == "start":
        pomo.pomodoro(todo_path, sys.argv[3])
    elif sys.argv[2] == "increment":
        pomo.increment(todo_path, sys.argv[3])
    elif sys.argv[2] == "decrement":
        pomo.decrement(todo_path, sys.argv[3])
    else:
        print("pydoro: Invalid input parameters..\n")
        print_help()
