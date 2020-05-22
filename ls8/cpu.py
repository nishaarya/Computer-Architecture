"""CPU functionality."""

import sys

class CPU:
    """Main CPU class."""

    # Implement the CPU constructor
    def __init__(self):
        self.registers = [0] * 8
        self.pc = 0
        self.ram = [0] * 256
        self.halted = False
        self.register[7] = 0xF4
        self.sp = 7

		# Construct a branch table
        # create a dictionary for the branch table
        self.branch_table = {}
        self.branch_table[LDI] = self.ldi
        self.branch_table[PRN] = self.prn
        self.branch_table[MUL] = self.mul
        self.branch_table[PUSH] = self.push
        self.branch_table[POP] = self.pop
    
    # Add RAM functions:
    # ram_read() - should accept the address to read and return the value stored there.
    # ram_write() - should accept a value to write, and the address to write it to.

    def ram_read(self, MAR):
        value = self.ram[MAR]
        return value

    def ram_write(self, MDR, MAR):
        self.ram[MAR] = MDR
    
    # Add the LDI instruction
    # load "immediate", store a value in a register, or "set this register to this value".
    def LDI(self):
        self.registers[self.ram_read(self.pc+1)] = self.ram_read(self.pc+2)

    # Add the PRN instruction
    # a pseudo-instruction that prints the numeric value stored in a register.
    def PRN(self):
        print(self.registers[self.ram_read(self.pc+1)])

    # Implement the HLT instruction handler
    # halt the CPU and exit the emulator.
    def HLT(self):
        self.halted = True

    def load(self):
        """Load a program into memory."""

        address = 0

    # Un-hardcode the machine code
        # Open a file
        with open(sys.argv[1]) as f:
            for line in f:
                # Remove '#' from output
                value = line.split("#")[0].strip()
                # Remove empty space from output
                if value == '':
                    continue
                v = int(value, 2)
                # Here we load it to memory
                self.ram[address] = v
                # Then we move on to the next
                address += 1
            
        


    def alu(self, op, reg_a, reg_b):
        """ALU operations."""

        if op == "ADD":
            self.registers[reg_a] += self.registers[reg_b]
        #elif op == "SUB": etc
        elif op == "MUL":
            self.registers[reg_a] *= self.registers[reg_b]
        else:
            raise Exception("Unsupported ALU operation")

    def trace(self):
        """
        Handy function to print out the CPU state. You might want to call this
        from run() if you need help debugging.
        """

        print(f"TRACE: %02X | %02X %02X %02X |" % (
            self.pc,
            #self.fl,
            #self.ie,
            self.ram_read(self.pc),
            self.ram_read(self.pc + 1),
            self.ram_read(self.pc + 2)
        ), end='')

        for i in range(8):
            print(" %02X" % self.reg[i], end='')

        print()

    # Implement the core of run()
    def run(self):
        # if it is not ending
        while not self.halted:
            # IR is the instruction register
            IR = self.ram_read(self.pc)
            # PC+1 and PC+2 from RAM into variables operand_a and operand_b
            operand_a = self.read_ram(self.pc + 1)
            operand_b = self.read_ram(self.pc + 2)
            
            # If the instruction register is ending
            if IR == HLT:
                # then end
                halted = True
            # or if the instruction register has an instruction to do
            elif IR in self.branch_table:
                # the instructions are in the branch_table
                # it will then run through operand_a and operand_b
                self.branch_table[IR](operand_a, operand_b)
                self.pc += (IR >> 6) + 1
            else:
                print("Instruction not recognized")
                sys.exit(1) 