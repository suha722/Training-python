"""
Import the subprocess module.
Define a variable cmd that contains the command to be run.
Use the subprocess.run() function to run the command and capture its output.
Print the output.
"""
import os
# import subprocess
# import time
#
# # print(os.getcwd())
# cmd=subprocess.run(['dir','tree'],capture_output=True)
# print(cmd.stdout)
# print(cmd.stderr)
# # cmd = subprocess.run(['ls', '-la','dne'],capture_output=True,text=True)
# # print(cmd.args)


from subprocess import run
#
# p = run( [ 'echo', 'Hello, world!' ] )
# print( 'exit status code:', p.returncode )
# Spawn a subprocess to execute the 'ls' command
'''process = subprocess.Popen(['ls', '-l'])

# Wait for the subprocess to finish and print its exit code
process.wait()
print('Exit code:', process.returncode)'''




'''import multiprocessing
# print(multiprocessing.cpu_count())
def sleep():
    time.sleep(1)
    print("Done")
if __name__=='__main__':
    start=time.perf_counter()
    p1=multiprocessing.Process(target=sleep)
    p2=multiprocessing.Process(target=sleep)
    p1.start()
    p2.start()
    p1.join()
    p2.join()
    end=time.perf_counter()
    print(f"Finished in {round(end-start,2)}")'''
# 2
'''def run_command(command):
    result = subprocess.run(command, capture_output=True, text=True)
    return result.stdout, result.returncode
commands = [
    ['echo', 'Command 1'],
    ['echo', 'Command 2'],
    ['echo', 'Command 3'],
]
for cmd in commands:
    print (run_command(cmd))
'''
#3
'''import multiprocessing

def circle_area(x):
    return 3.14 * x ** 2
if __name__=="__main__":
# Create a pool of worker processes
    pool = multiprocessing.Pool()

    # Map the circle_area function over a list of numbers
    results = pool.map(circle_area, [2,4,6,1])

    # Print the results
    print("The circular arae of radios [2,4,6,1] is :",results)

'''
import subprocess

# result = subprocess.run(["dir"], shell=True, capture_output=True, text=True)
#
# print(result.stdout)


result = subprocess.run(["echo","hello,world!"],capture_output=True,text=True ,shell=True)

print(result.stdout)
# print(result)