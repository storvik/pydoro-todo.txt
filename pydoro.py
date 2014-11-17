#!/usr/local/bin/python3

import os
import sys

import pomo

# Configuration parameters
work_time = 25
break_short = 5
break_long = 20
audio_file = "/Users/storvik/developer/pydoro-todo.txt/pomo.wav"

if __name__ == '__main__':

    todo_path = os.environ.get('TODO_DIR')

    if len(sys.argv) < 3:
        print("pydoro: Wrong input...")
        exit(-1)

    if sys.argv[2] == "ls":
        pomo.listpm(todo_path)
    elif sys.argv[2] == "start":
        pomo.pomodoro(todo_path,sys.argv[3])
