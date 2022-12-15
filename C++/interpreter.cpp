#include <iostream>
#include <fstream>
#include <sstream>

int main(int argc, char *argv[])
{
    try
    {
        int mem[30000]; // max bytes 
        int memPos = 0;

        std::ifstream file(argv[1]);
        std::stringstream buffer;
        std::string command;

        buffer << file.rdbuf();
        command = buffer.str();

        int count = 0;

        while (count < command.length())
        {
            if(command[count] == '>') { memPos += 1; }

            else if(command[count] == '<') { memPos -= 1; }  

            else if(command[count] == '+') { 
                mem[memPos] += 1;
                        
                if(mem[memPos] > 255){
                    mem[memPos] = 0;
                }
            }

            else if(command[count] == '-') { 
                mem[memPos] = 1;
                        
                if(mem[memPos] > 255){
                    mem[memPos] = 0;
                }
            }   

            else if(command[count] == '.') { std::cout << ((char)mem[memPos]); }   

            else if(command[count] == ',') { 
                char input;
                std::cin >> input;

                mem[memPos] = (int)input;
            }  

            count++; 
        }
    }

    catch(...)
    {
        std::cout << "Error";
    }
}