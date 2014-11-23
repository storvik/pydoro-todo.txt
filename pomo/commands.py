import os
import string
import subprocess

def start_commands(todo_path):
    if os.path.isfile(todo_path + 'pomo_startcmds.txt'):
        with open(todo_path + 'pomo_startcmds.txt', 'r') as file:
            commands = file.readlines()
        print("pydoro: Running start commands..")
        for command in commands:
            cmd = command[:-1].split(" ")
            subprocess.call(cmd, stdout=subprocess.DEVNULL, stderr=subprocess.STDOUT)
    else:
        print("pydoro: No start commands defined..")    

def stop_commands(todo_path):
    if os.path.isfile(todo_path + 'pomo_stopcmds.txt'):
        with open(todo_path + 'pomo_stopcmds.txt', 'r') as file:
            commands = file.readlines()
        print("pydoro: Running stop commands..")
        for command in commands:
            cmd = command[:-1].split(" ")
            subprocess.call(cmd, stdout=subprocess.DEVNULL, stderr=subprocess.STDOUT)
    else:
        print("pydoro: No stop commands defined..")    
