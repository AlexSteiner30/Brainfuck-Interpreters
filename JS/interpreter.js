var fs = require('fs');

function main()
{
        let mem = [] 
        let memPos = 0;

        for (var i = 0; i < 3000; i++) { // max bytes
            mem.push(i);
        }

        let file = fs.readFileSync("brainfuck.bf");
        var command = file.toString();

        var count = 0;

        while (count < command.length) {
            if (command[count] == '>') {
                memPos += 1;
            }

            else if (command[count] == '<') {
                memPos -= 1;
            }

            else if (command[count] == '+') {
                mem[memPos] += 1;
                
                if (mem[memPos] > 255) {
                    mem[memPos] = 0;
                }
            }

            else if (command[count] == '-') {
                mem[memPos] = 1;

                if (mem[memPos] > 255) {
                    mem[memPos] = 0;
                }
            }

            else if (command[count] == '.') {
                console.log(String.fromCharCode(mem[memPos]));
            }

            else if (command[count] == ',') {
                let input = prompt();
                mem[memPos] = input;
            }

            count++;
        }
  
}

main();