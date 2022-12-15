
def main():
    try:
        mem = [] 
        memPos = 0;


        count = 0;

        while count < command.length:
            if (command[count] == '>'):
                memPos += 1;

            elif (command[count] == '<'):
                memPos -= 1;
            
            elif (command[count] == '+'):
                mem[memPos] += 1;
                
                if (mem[memPos] > 255):
                    mem[memPos] = 0;

            elif command[count] == '-':
                mem[memPos] = 1;

                if mem[memPos] > 255:
                    mem[memPos] = 0;

            elif command[count] == '.':
                console.log(String.fromCharCode(mem[memPos]));

            elif command[count] == ',':
                input = input();
                mem[memPos] = input;
     
            count+=1
    except:
        print("Erorr")
  
if __name__ == "__main__":
	main()