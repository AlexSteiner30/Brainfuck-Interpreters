
def main():
    try:
        mem = [] 
        memPos = 0 

        for i in range (30000):
            mem.append(i);


        count = 0

        command = open('brainfuck.bf').read()

        while count < len(command):
            if (command[count] == '>'):
                memPos += 1

            elif (command[count] == '<'):
                memPos -= 1
            
            elif (command[count] == '+'):
                mem[memPos] += 1
                
                if (mem[memPos] > 255):
                    mem[memPos] = 0

            elif command[count] == '-':
                mem[memPos] = 1

                if mem[memPos] > 255:
                    mem[memPos] = 0;

            elif command[count] == '.':
                print(chr(mem[memPos]), end="");

            elif command[count] == ',':
                input = input();
                mem[memPos] = input;
     
            count+=1
    except:
        print("Error")

if __name__ == "__main__":
	main()