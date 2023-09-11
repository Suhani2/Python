import os

def traverse_directory(path):
    for root, directories, files in os.walk(path):
        # Print the current directory
        print(f"Directory: {root}")

        # Print all files in the current directory
        for file in files:
            file_path = os.path.join(root, file)
            print(f"File: {file_path}")

directory_path = r"C:\Users\suhan\AppData\Local\JetBrains\PyCharmCE2023.1"
traverse_directory(directory_path)