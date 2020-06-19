"""CPU functionality."""

import sys

class CPU:
    """Main CPU class."""

    def __init__(self):
        """Construct a new CPU."""
        self.reg = [0] * 8
        self.ram = [0] * 256
        self.pc = 0
        self.L = False
        self.G = False
        self.E = False

    def load(self, program):
        """Load a program into memory."""

        address = 0

        for instruction in program:
            self.ram[address] = instruction
            address += 1

    def run(self):
        """Run the CPU."""
        LDI = 0b10000010
        CMP = 0b10100111
        JMP = 0b01010100
        JEQ = 0b01010101
        JNE = 0b01010110
        PRN = 0b01000111
        HLT = 0b00000001

        halted = False

        while not halted:
            instruction = self.ram[self.pc]

            if instruction == LDI:
                reg_num = self.ram[self.pc + 1]
                value = self.ram[self.pc + 2]

                self.reg[reg_num] = value

                self.pc += 3

            elif instruction == PRN:
                reg_num = self.ram[self.pc + 1]
                print("PRINT ", self.reg[reg_num])
                self.pc += 2

            elif instruction == CMP:
                reg_a = self.ram[self.pc + 1]
                reg_b = self.ram[self.pc + 2]

                comp_a = self.reg[reg_a]
                comp_b = self.reg[reg_b]

                if comp_a < comp_b:
                    self.L = True
                elif comp_a > comp_b:
                    self.G = True

                if comp_a == comp_b:
                    self.E = True
                else:
                    self.E = False

                self.pc += 3

            elif instruction == JMP:
                reg_num = self.ram[self.pc + 1]
                self.pc = self.reg[reg_num]

            elif instruction == JEQ:
                if self.E == True:
                    reg_num = self.ram[self.pc + 1]
                    self.pc = self.reg[reg_num]
                else:
                    self.pc += 2

            elif instruction == JNE:
                if self.E == False:
                    reg_num = self.ram[self.pc + 1]
                    self.pc = self.reg[reg_num]
                else:
                    self.pc += 2

            elif instruction == HLT:
                halted = True
