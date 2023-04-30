class FileWriter:
    def write_to_file(self, content, filename):
        try:
            with open(filename, 'w', encoding='utf-8') as f:
                f.write(content)
        except Exception as e:
            print(f"Error writing content to file '{filename}': {e}")
