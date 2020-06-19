# #!/usr/bin/env python3

"""Main."""

import sys
from cpu import *

cpu = CPU()
file = open("sctest.ls8", "r")
program = []
for instruction in file:
    print(instruction)
    # byte = instruction.split()[0]
    # print(byte, "for byte") 
    # if byte != '#':
    #     byte = int(byte, base=2)
    #     program.append(byte)

cpu.load(program)
cpu.run()