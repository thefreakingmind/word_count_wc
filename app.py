from setuptools import setup, find_packages
import sys

print(dir(sys))

class FileReader(object):
    def __init__(self, file_name, instruction):
        self.file_name = file_name
        self.instruction = instruction 

    def read_file(self):
        with open (self.file_name, self.instruction, encoding="utf-8") as fh:
            return fh.read()



class CalculationProcessor(object):
    def __init__(self, data):
        self.data = data

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


file_reader = FileReader("input_text.txt", "r")
data = file_reader.read_file()
calculation = CalculationProcessor(data)
calculation.read_lines()
