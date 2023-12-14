import time
from colorama import Fore
def system_run(line, variables):
    if line[0] == "exit":
        exit()
    elif line[0] == "calculate":
        calcula = ' '.join(line[1:])
        
        print(eval(calcula.replace("'", "")))
    elif line[0] == 'sleep':
        time.sleep(int(line[1]))
    else:
        return