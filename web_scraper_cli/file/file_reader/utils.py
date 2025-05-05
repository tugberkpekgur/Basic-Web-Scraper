import os


def is_file_exists(file_path: str) -> bool:
    """
    Check if a file exists at the given path.
    """
    return os.path.isfile(file_path)

def read_file_lines(file_path: str) -> list:
    """
    Read the content of a file and return it as a list of lines.
    """
    try:
        with open(file_path, 'r') as file:
            lines = file.readlines()
        return lines
    except FileNotFoundError:
        print(f"File not found: {file_path}")
        return None
    except IOError as e:
        print(f"Error reading file {file_path}: {e}")
        return None
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return None