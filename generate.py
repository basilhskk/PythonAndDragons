import argparse 
import os
from pathlib import Path
from logger import TerminalColors

def banner():

    print(TerminalColors.CYAN+"  _____       _   _                            _____                                  "+TerminalColors.ENDC)
    print(TerminalColors.CYAN+" |  __ \     | | | |                   ___    |  __ \                                 "+TerminalColors.ENDC)
    print(TerminalColors.CYAN+" | |__) |   _| |_| |__   ___  _ __    ( _ )   | |  | |_ __ __ _  __ _  ___  _ __  ___ "+TerminalColors.ENDC)
    print(TerminalColors.CYAN+" |  ___/ | | | __| '_ \ / _ \| '_ \   / _ \/\ | |  | | '__/ _` |/ _` |/ _ \| '_ \/ __|"+TerminalColors.ENDC)
    print(TerminalColors.CYAN+" | |   | |_| | |_| | | | (_) | | | | | (_>  < | |__| | | | (_| | (_| | (_) | | | \__ \\"+TerminalColors.ENDC)
    print(TerminalColors.CYAN+" |_|    \__, |\__|_| |_|\___/|_| |_|  \___/\/ |_____/|_|  \__,_|\__, |\___/|_| |_|___/"+TerminalColors.ENDC)
    print(TerminalColors.CYAN+"         __/ |                                                   __/ |                "+TerminalColors.ENDC)
    print(TerminalColors.CYAN+"        |___/                                                   |___/                 "+TerminalColors.ENDC)

   
def arg_parser():

    banner()

    usage_text = '''usage:

    python3 PnD.py /path/to/pyi
    ./PnD.py ../path/to/Pyinstaller/ # relative ppath
    '''

    parser = argparse.ArgumentParser(description="Pythons and Dragons Pyinstaller static analysis bypass tool ",epilog=usage_text,formatter_class=argparse.RawDescriptionHelpFormatter)

    parser.add_argument('script', type=str, help='Script you want to make executable')

    parser.add_argument('-p','--path', type=str, help='Where to create pyinstaller directory (Default: home of current user)')

    args = parser.parse_args()

    return args


def generate_exe(installation_path,script,options=[]):
    pyi = os.path.join(installation_path,"pyinstaller.py")
    os.system(f"python {pyi} --console --onefile --noconfirm --version-file ./versionFile.txt {script}")


if __name__ == '__main__':
    
    args = arg_parser()
    folder = args.path
    script = args.script

    if not folder:
        user_directory = str(Path.home())
        folder=os.path.join(user_directory,"pyinstaller","pyinstaller-4.0")

    generate_exe(folder,script)
