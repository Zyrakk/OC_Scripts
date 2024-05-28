#!/bin/python3
# Script to stress CPU

import argparse
from multiprocessing import Pool, cpu_count, freeze_support, set_start_method
from threading import Event
import signal
import sys

# Pool functions
# CPU stress
def f(x):
    while True:
        x * x

# Main function
if __name__ == '__main__':
    freeze_support()
    set_start_method('spawn')
    
    # Read arguments
    parser = argparse.ArgumentParser(description='Script to run very simple CPU stress tests')
    parser.add_argument('--cpu', dest='cpus', type=int, default=2, help='number of CPU threads to stress (default: 6). Use -1 to stress all the CPUs')
    parser.add_argument('--time', dest='time', type=int, default=18, help='Time for the test in seconds (default: 1800)')

    args = parser.parse_args()

    # Signal wrapper to stop tests
    global poolc
    global sleep
    poolc = None  # workers for CPU stress
    sleep = Event()  # event is used to have an interruptible sleep

    def exit_chld(x, y):
        global poolc
        global sleep
        if poolc is not None:
            poolc.terminate()
        sleep.set()

    signal.signal(signal.SIGINT, exit_chld)

    if args.cpus != 0:
        if args.cpus < 0:
            args.cpus = cpu_count()

        processes = args.cpus
        print("Running load on CPU...\nUtilizing %d cores" % processes)

        poolc = Pool(processes)
        poolc.map_async(f, range(processes))

    # Exit after seconds
    print("Working for %d seconds" % args.time)
    sleep.wait(args.time)
    exit_chld(0, 0)
    sys.exit(0)
