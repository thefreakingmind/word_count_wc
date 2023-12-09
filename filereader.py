import os 

class FileReader(object):
    def __init__(self, file_name, instruction):
        self.file_name = file_name
        self.instruction = instruction 
        self.file_header = None

    def read_file(self):
        with open (self.file_name, self.instruction, encoding="utf-8") as fh:
            return fh.read()

    def calculate_file_header_size(self):
        return self.file_header

    def process_file(self):
        return self.file_header
