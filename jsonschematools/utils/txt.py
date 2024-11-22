def read_text_file(filepath: str) -> str:
    with open(filepath, 'r') as file:
        return file.read()
