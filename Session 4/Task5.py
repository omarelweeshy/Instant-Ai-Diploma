import fileinput

file_path = 'osos.txt'
line_number_to_insert = int(input("Enter the number of the line to modify: "))
new_line = input("Enter your new line: ") + '\n'

with fileinput.FileInput(file_path, inplace=True, backup='.bak') as file:
    for current_line_number, line in enumerate(file, 1):
        if current_line_number == line_number_to_insert:
            print(new_line, end='')
        print(line, end='')

print("File has been updated.")
