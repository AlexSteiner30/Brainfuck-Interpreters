import java.util.Scanner;
import java.io.*;

class Interpreter {
    public static void main(String[] args) {
        try {
            int[] mem = new int[30000]; // max bytes
            int memPos = 0;

            String command = "";
            Scanner file = new Scanner(new File(args[0]));

            while (file.hasNext()) {
                command += file.nextLine();
            }

            file.close();

            int count = 0;

            while (count < command.length()) {
                if (command.charAt(count) == '>') {
                    memPos += 1;
                }

                else if (command.charAt(count) == '<') {
                    memPos -= 1;
                }

                else if (command.charAt(count) == '+') {
                    mem[memPos] += 1;

                    if (mem[memPos] > 255) {
                        mem[memPos] = 0;
                    }
                }

                else if (command.charAt(count) == '-') {
                    mem[memPos] = 1;

                    if (mem[memPos] > 255) {
                        mem[memPos] = 0;
                    }
                }

                else if (command.charAt(count) == '.') {
                    System.out.println((char) mem[memPos]);
                }

                else if (command.charAt(count) == ',') {
                    Scanner scanner = new Scanner(System.in);
                    mem[memPos] = Integer.valueOf(scanner.nextLine());
                    scanner.close();
                }

                count++;
            }
        }

        catch (Exception e) {
            System.out.println(e);
        }
    }
}