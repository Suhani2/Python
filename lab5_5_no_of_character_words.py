def analyze_text_file(file_path):
    try:
        with open(file_path, 'r') as file:
            content = file.read()

            char_count = len(content)
            word_count = len(content.split())
            # space_count = content.count(' ')
            # line_count = content.count('\n')

            print("File analysis summary:")
            print("Character count:", char_count)
            print("Word count:", word_count)
            # print("Space count:", space_count)
            # print("Line count:", line_count)

    except FileNotFoundError:
        print("File not found!")

file_path = "lab5_1.txt"
analyze_text_file(file_path)