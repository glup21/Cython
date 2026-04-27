import sys
from compiler import project_compile
from virtual_machine import project_exec

input = sys.argv[1]
output = sys.argv[2]

project_compile(input, output)
project_exec(output)
