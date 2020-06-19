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
        # program = [
        #     10000010, # LDI R0,10
        #     00000000,
        #     0b00001010,
        #     10000010, # LDI R1,20
        #     0b00000001,
        #     0b00010100,
        #     10000010, # LDI R2,TEST1
        #     0b00000010,
        #     0b00010011,
        #     10100111, # CMP R0,R1
        #     00000000,
        #     0b00000001,
        #     0b01010101, # JEQ R2
        #     0b00000010,
        #     10000010, # LDI R3,1
        #     0b00000011,
        #     0b00000001,
        #     0b01000111, # PRN R3
        #     0b00000011,
        #     # TEST1 (address 19):
        #     10000010, # LDI R2,TEST2
        #     0b00000010,
        #     0b00100000,
        #     10100111, # CMP R0,R1
        #     00000000,
        #     0b00000001,
        #     0b01010110, # JNE R2
        #     0b00000010,
        #     10000010, # LDI R3,2
        #     0b00000011,
        #     0b00000010,
        #     0b01000111, # PRN R3
        #     0b00000011,
        #     # TEST2 (address 32):
        #     10000010, # LDI R1,10
        #     0b00000001,
        #     0b00001010,
        #     10000010, # LDI R2,TEST3
        #     0b00000010,
        #     0b00110000,
        #     10100111, # CMP R0,R1
        #     00000000,
        #     0b00000001,
        #     0b01010101, # JEQ R2
        #     0b00000010,
        #     10000010, # LDI R3,3
        #     0b00000011,
        #     0b00000011,
        #     0b01000111, # PRN R3
        #     0b00000011,
        #     # TEST3 (address 48):
        #     10000010, # LDI R2,TEST4
        #     0b00000010,
        #     0b00111101,
        #     10100111, # CMP R0,R1
        #     00000000,
        #     0b00000001,
        #     0b01010110, # JNE R2
        #     0b00000010,
        #     10000010, # LDI R3,4
        #     0b00000011,
        #     0b00000100,
        #     0b01000111, # PRN R3
        #     0b00000011,
        #     # TEST4 (address 61):
        #     10000010, # LDI R3,5
        #     0b00000011,
        #     0b00000101,
        #     0b01000111, # PRN R3
        #     0b00000011,
        #     10000010, # LDI R2,TEST5
        #     0b00000010,
        #     0b01001001,
        #     0b01010100, # JMP R2
        #     0b00000010,
        #     0b01000111, # PRN R3
        #     0b00000011,
        #     # TEST5 (address 73):
        #     0b00000001 # HLT
        #     ]
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
