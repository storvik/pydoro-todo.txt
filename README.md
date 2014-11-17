pydoro-todo.txt
===============

Simple pomodoro timer for the todo.txt-cli implemented in python.
Port of pomodori-todo.txt to python.
Tested on a Macbook Pro with python 3.4.

[Todo.txt-cli](https://github.com/ginatrapani/todo.txt-cli)

[Pomodori-todo.txt](https://github.com/metalelf0/pomodori-todo.txt)

Features
--------

- List todos
- Start pomodoros
- Start/stop time logged to pydoro.log in todo folder

Installation
------------

Clone git repository.
```sh
$ git clone git@github.com:storsnik/pydoro-todo.txt.git
```
Create symlink to you TODO_ACTIONS_DIR.
```sh
$ ln -s /path/to/pydoro.py /path/to/TODO_ACTIONS_DIR/pd
```

Usage
-----
```sh
$ todo.txt pd [arguments]
```

|Arguments       | Description                     |
|----------------|---------------------------------|
| ls             | List undone todo-files          |
| start [number] | Start pomodoro on task [number] |


