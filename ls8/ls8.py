# #!/usr/bin/env python3

"""Main."""

import sys
from cpu import *

cpu = CPU()
program = []
for instruction in program:
    print(instruction)
    byte = instruction.split()[0]
    print(byte, "for byte") 
    if byte != '#':
        byte = int(byte, base=2)
        program.append(byte)

cpu.load(program)
cpu.run()