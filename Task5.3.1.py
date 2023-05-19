from concurrent.futures import ProcessPoolExecutor
import logging
import subprocess


def file_command(filename):
    try:
        with open(filename, "r") as file:
            for _ in file:
                line = file.read()
    except FileNotFoundError as e:
        print("Sorry this file not found! ")
    return line
def execute():
    # list_file=["input.txt","github.ico"]
    # with ProcessPoolExecutor()as executor:
    #     prcs=executor.map(file_command,list_file)
    #     for result in prcs:
    #         print(result)

    data = file_command("input.txt")
    command_data = data.split("\n")
    # print(command_data)
    logging.basicConfig(filename="output_command.log", filemode="a",
                        format="'%(asctime)s'|The Process id: '%(process)d-'| "
                               "%(levelname)s|The result of command is \n'%(message)s'",
                        datefmt='%d-%b-%y %H:%M:%S')
    # logging.error("this error message")
    for cmd in command_data:
        try:
            p1 = subprocess.run(cmd, capture_output=True, text=True, shell=True)
            print(p1.returncode)
            if p1.returncode==0 or p1.stderr!=None:
                logging.critical(p1.stdout)
            else:
                logging.error(p1.stderr)
            print(p1.stdout)
            p1.kill
        except Exception:
            print("The command is not found ")
execute()