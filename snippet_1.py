import os
import subprocess

# a= subprocess.Popen('ps aux')
a = os.popen("ps aux")
print(a.readline())
b = a.readline()
b = b.split()
print(b)
