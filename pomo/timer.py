import sys
import time
import string

# Start pomodoro timer
def timer(duration):
    try:
        prog_bar = "*"+" "*(duration-1)
        sys.stdout.write("(%s) Remaining: %.0f minutes" % (prog_bar, 24))
        for i in range(duration):
            prog_bar = prog_bar[:i+1].replace(" ", "*") + prog_bar[i+1:]
            remaining = duration-(i+1)
            sys.stdout.write("\r(%s) Remaining: %.0f minutes" % (prog_bar, remaining))
            sys.stdout.flush()
            time.sleep(1) # Replace with 60 in finished addon
    except KeyboardInterrupt:
        print("\npydoro: Exiting..")
        exit(-1)
