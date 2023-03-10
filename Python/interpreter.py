import sys

def main(*argv):
        mem = [0]
        memPos = 0 

        count = 0

        command = open(sys.argv[1]).read()

        while count < len(command):
            if (command[count] == '>'):
                memPos += 1

                if(len(mem) <= memPos + 1):
                    mem.append(0)
                
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
                try:
                    print(chr(mem[memPos]), end="");
                except:
                    print((mem[memPos]), end="");

            elif command[count] == ',':
                inputTxt = input()
                mem[memPos] = inputTxt

            elif command[count] == "[":
               mem.append(0)
               print(mem[memPos + 1])
				
            elif command[count] == "]":
                pass
            
            count+=1

if __name__ == "__main__":
	main()