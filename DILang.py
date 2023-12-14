from colorama import Fore
from console import console_run
from system import system_run
def run(file):
    def process(tokens):
            if tokens[0] == '#':
                return
            if tokens[0] == 'console':
                var = console_run(tokens[1:], variables)
                return var
            elif tokens[0] == 'system':
                var = system_run(tokens[1:], variables)
                return var
            else:
                return "exit"
    variables = {}
    line_count = 0
    try:
        with open(file, 'r') as file:
            lines = file.readlines()
    except Exception as e:
        print(Fore.RED+(f'Error: {e}'))
        print(Fore.RESET)
        exit(1)
    for line in lines:
        line_count += 1
        tokenss = line.strip().split()
        if line.strip() == "":
            continue
        if line.split()[1] == "=":
            if not tokenss[3].startswith("'"):
                tokenss=tokenss[2:]
                print(tokenss)
                r = process(tokenss)
                print(r)
                variables = {f"{line[0]}": r}
                continue
            variables = {f"{tokenss[0]}": line[3:].replace("'", '')}
        k = process(tokenss)
        if k == "exit":
            print(Fore.RED+(f'Error: Unknown command: {tokens[0]} On line {line_count}'))
            print(Fore.RESET)
            exit(1)
            
