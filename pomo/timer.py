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
            remaining_min = duration-(i+1)
            for sek in range(0,60):
                remaining_sek = 60 - sek
                sys.stdout.write("\r(%s) Remaining: %.0f min %.0f sek" % (prog_bar, remaining_min, remaining_sek))
                sys.stdout.flush()
                time.sleep(1)
    except KeyboardInterrupt:
        print("\npydoro: Exiting..")
        exit(-1)
