# A simple virtual CPU
# A program that pretends to be a CPU

#  Instructions
#  * Print "Nish" on the screen - three times
#  * Halts the program - ends it

import sys

# Set variables for instructions
PRINT_NISH = 1 # print nish is instruction 1
HALT = 2 # halt is instruction 2
SAVE_REG = 3 # save register is instruction 3
PRINT_REG = 4 #  print register is instruction 4
ADD = 5 # add is instruction 5

# create our list which is called memory - this is where we will put our program
memory = [
    PRINT_NISH,
    SAVE_REG, # save_reg r0, 12
    0, # I want to save it in register 0
    37, # this is the address the PC is 'pointing' at
    SAVE_REG,
    1, 
    12,
    ADD, # this is adding the two registers, adding the above register 0 to register 1
    0,
    1,
    PRINT_REG, # print register R0
    0,
    PRINT_NISH, # print Nish again
    HALT
    ]

# create register variables, names R0-R7
registers = [0,0,0,0,0,0,0,0]
​
# To start, running will be true (can also be written as running = True)
halted = False

# Program counter - index into memory array, starts at 0
# AKA as pointer, address or location
pc = 0 

# Load the program from instructionfilecomp.py
with open("instructionfilecomp") as f:
    for line in f:
        # this removes the '#' and only outputs the int numbers
        string_val = line.split('#')[0]
        # and this continues running even if the string has empty sapce '
        if string_val == '':
            continue
        print(line)

sys.exit(0)

# so whilst we have NOT ended
while not halted: 
    # lets start off with instruction that 
    instruction = memory[pc]

    # print Nish!
    if instruction == PRINT_NISH:
        print("Nish!")
        # then move to the next instruction from the first pointer
        pc =+ 1
    
    # if not print Nish!
    elif instruction == HALT:
        halted = True
    
    elif instruction == SAVE_REG:
        # the register number we want to save things in
        # in the memory array, reg_num is after save_reg, so +1
        reg_num = memory[pc + 1]
        # the value we want to store them
        # in the memory array, value is 2 after save_reg, so +2
        value = memory[pc + 2]

        # got reg_num, so can store value
        registers[reg_num] = value

        # now we need to move the PC by 3
        pc += 3

    elif instruction == PRINT_REG:
        # register number is after the print_reg, so pc goes + 1
        reg_num = memory[pc + 1]
        print(registers[reg_num])

        pc += 2
    
    # if instruction is unknown, print and show at which address the instrustion is coming from
    else:
        print(f'unknown instruction {instruction} at address {pc}')
        # and then exit to come out of program
        exit(1)