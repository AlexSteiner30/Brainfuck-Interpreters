program = input()

tape = [0]
cell_index = 0

pointer = 0
while pointer < len(program):
	instruction = program[pointer]
	if instruction == "+":
		tape[cell_index] += 1
		if tape[cell_index] == 256:
			tape[cell_index] = 0

	elif instruction == "-":
		tape[cell_index] -= 1
		if tape[cell_index] == -1:
			tape[cell_index] = 255

	elif instruction == "<":
		cell_index -= 1

	elif instruction == ">":
		cell_index += 1

	elif instruction == ".":
		print(chr(tape[cell_index]), end="")
	
	pointer += 1