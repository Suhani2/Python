import os

def find_text_files_with_substring(root_directory, substring):
    matching_files = []

    for root, directories, files in os.walk(root_directory):
        for file in files:
            if file.endswith(".txt"):  # Filter for text files
                file_path = os.path.join(root, file)
                with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
                    file_content = f.read()
                    if substring in file_content:
                        matching_files.append(file_path)

    return matching_files

# Specify the root directory and the substring to search for
root_directory = r"C:\Users\suhan\AppData\Local\JetBrains\PyCharmCE2023.1"
substring = " "
matching_files = find_text_files_with_substring(root_directory, substring)

for file in matching_files:
    print(file)