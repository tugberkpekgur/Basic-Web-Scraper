import os
import utils

class read_file:
    def __init__(self, file_path: str) -> None:
        self.file_path = file_path
        self.file_name = os.path.basename(file_path)
        self.url = read_file()
        
    def read_file(self) -> list:
        """
        Read the content of a file and return it as a list of lines.
        """
        if not utils.is_file_exists(self.file_path):
            print(f"File not found: {self.file_path}")
            return None
        self.lines = utils.read_file_lines(self.file_path)
        if self.lines is None:
            print(f"Error reading file {self.file_path}")
            return None
        return self.lines
    

        
    
    
    
        
        
        