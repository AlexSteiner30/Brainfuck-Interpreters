using System;
using System.IO;
using System.Collections;
using System.Collections.Generic;

class Interpreter
{
    private static void Main(string[] args)
    {
        try
        {
            int[] mem = new int[30000]; // max bytes 
            int memPos = 0;

            string command = File.ReadAllText(args[0]); 
            int count = 0;

            while (count < command.Length)
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

                else if(command[count] == '.') { Console.Write((char)mem[memPos]); }   

                else if(command[count] == ',') { 
                    mem[memPos] = System.Convert.ToInt32(Console.Read().ToString());
                }  

                count++; 
            }
        }

        catch(Exception e)
        {
            Console.WriteLine(e);
        }
    }
}