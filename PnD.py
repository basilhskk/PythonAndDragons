#!/usr/bin/env python3
# Pyinstaller Customizer Tool as described in Python and Dragons Paper
import argparse
import psutil
import os

class TermColors:
    HEADER = '\033[95m'
    BLUE = '\033[94m'
    CYAN = '\033[96m'
    OK = '\033[92m' # Green
    WARNING = '\033[93m' #Red
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

def is_running_in_powershell():
    parent_pid = os.getppid()
    process = psutil.Process(parent_pid)
    if "powershell" in process.name().lower():
        return True
    return False



def banner():

    print(TermColors.CYAN+"  _____       _   _                            _____                                  "+TermColors.ENDC)
    print(TermColors.CYAN+" |  __ \     | | | |                   ___    |  __ \                                 "+TermColors.ENDC)
    print(TermColors.CYAN+" | |__) |   _| |_| |__   ___  _ __    ( _ )   | |  | |_ __ __ _  __ _  ___  _ __  ___ "+TermColors.ENDC)
    print(TermColors.CYAN+" |  ___/ | | | __| '_ \ / _ \| '_ \   / _ \/\ | |  | | '__/ _` |/ _` |/ _ \| '_ \/ __|"+TermColors.ENDC)
    print(TermColors.CYAN+" | |   | |_| | |_| | | | (_) | | | | | (_>  < | |__| | | | (_| | (_| | (_) | | | \__ \\"+TermColors.ENDC)
    print(TermColors.CYAN+" |_|    \__, |\__|_| |_|\___/|_| |_|  \___/\/ |_____/|_|  \__,_|\__, |\___/|_| |_|___/"+TermColors.ENDC)
    print(TermColors.CYAN+"         __/ |                                                   __/ |                "+TermColors.ENDC)
    print(TermColors.CYAN+"        |___/                                                   |___/                 "+TermColors.ENDC)

    
def argParser():
    banner()
    parser = argparse.ArgumentParser(description="test"+TermColors.ENDC)
    parser.add_argument('integers', metavar='N', type=int, nargs='+',
                        help='an integer for the accumulator')
    parser.add_argument('--sum', dest='accumulate', action='store_const',
                        const=sum, default=max,
                        help='sum the integers (default: find the max)')

    args = parser.parse_args()
    # print(args.accumulate(args.integers))
    return args


if __name__ == '__main__':
    isRunnigInPowershell()

    args = argParser()
    isRunnigInPowershell()