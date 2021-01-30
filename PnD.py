#!/usr/bin/env python3
# Pyinstaller Customizer Tool as described in Pythons and Dragons Paper
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

    
def arg_parser():
    banner()

    usage_text = '''usage:

    python3 PnD.py C:/path/to/Pyinstaller/Directory # full path
    ./PnD.py ../path/to/Pyinstaller/ # relative ppath
    '''

    parser = argparse.ArgumentParser(description="Pythons and Dragons Pyinstaller static analysis evasion tool ",epilog=usage_text,formatter_class=argparse.RawDescriptionHelpFormatter)

    parser.add_argument('-d','--download', help='Enter version of Pyinstaller that you want to make stealth Default and RECOMMENDED :4.0',default="0") # TODO

    parser.add_argument('direcoty', help='Directory of Pyinstaller that you want to make stealth')

    args = parser.parse_args()

    return args


if __name__ == '__main__':
    args = arg_parser()
