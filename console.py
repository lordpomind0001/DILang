from colorama import Fore
import subprocess
def console_run(line, variables):
    if line[0] == 'send':
        if line[1] in variables:
            text = variables[f"{line[1]}"]
        else:
            text = ' '.join(line[1:])
        #print(variables)
        #print(text)
        print(text.replace("'", ""))
    elif line[0] == 'clear':
        subprocess.run('clear')
    elif line[0] == 'input':
        return input()
    else:
        return