from setuptools import setup, find_packages
import sys
import os 
from pathlib import Path
from filereader import FileReader

class CalculationProcessor(object):
    def __init__(self, data, file_name, instruction):
        self.data = data
        self.file_name = file_name 
        self.instruction = instruction
        # Handle with some different logic
        print(len(sys.argv))
        if sys.argv is not None and len(sys.argv) > 1:
            self.arguements =  sys.argv[1]
        else:
            print("Argument is not present")
            self.arguments = None

    def calculate_file_size(self):
        fileData = os.stat(self.file_name)
        # print(dir(fileData))
        return fileData.st_size
    
    def calculate_arguement(self):
        if self.validate_argument_length() and self.arguements == '-c':
            return self.calculate_bytes()
        elif self.validate_argument_length() and self.arguements == '-l':
            return self.calculate_lines()
        elif self.validate_argument_length()  and self.arguements == '-w':
            return self.calculate_word()
        elif  self.validate_argument_length()  and self.arguements == None:
            return self.read_lines()
        else:
            print("Invalid Arguement passed in the command")

    def validate_argument_length(self):
        if len(sys.argv) > 1:
            return True
        else:
            return False


    def calculate_lines(self):
        line_length = 0
        with open (self.file_name, self.instruction, encoding="utf-8") as fh:
            print(len(fh.readline()))
        return line_length

    def calculate_bytes(self):
        tiny_byte = 0
        # print(self.data)
        for line in self.data:
            tiny_byte += len(line)
        return tiny_byte 

    def calculate_word(self):
        for line in self.data:
            word += len(line.split()) 
        return word

    def read_lines(self):
        word = 0
        line_length = 0
        character = 0
        for line in self.data:
            if line is not None:
                line_length +=1
                word += len(line.split())
                character += len(line)

        print("Length of line is  ", line_length)
        print("Length of word is ",  word)
        print("Length of Character is ",  character)


if __name__ == '__main__':
    file_reader = FileReader("input_text.txt", "r")
    data = file_reader.read_file()
    calculation = CalculationProcessor(data, "input_text.txt",'r' )
    # calculation.read_lines()
    calculation.calculate_lines() 
    calculation.calculate_arguement()
    x = calculation.calculate_file_size()
    print(x)
