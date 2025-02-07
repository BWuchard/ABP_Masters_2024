import sys

def read_first_line(file_name):
    with open(file_name, 'r') as file:
        lines = file.readlines()
        if lines:
            return lines[0].strip()  # Return the first line without leading/trailing whitespaces
        else:
            return None

def read_second_and_third_lines(file_names):
    second_and_third_lines = []
    for file_name in file_names:
        with open(file_name, 'r') as file:
            lines = file.readlines()
            if len(lines) >= 2:
                second_and_third_lines.append(lines[1].strip())
            if len(lines) >= 3:
                second_and_third_lines.append(lines[2].strip())
    return second_and_third_lines

def main(output_file, file_names):
    first_line = read_first_line(file_names[0])
    if first_line:
        with open(output_file, 'w') as output:
            output.write(first_line + '\n')
            second_and_third_lines = read_second_and_third_lines(file_names[0:])
            for line in second_and_third_lines:
                output.write(line + '\n')
        print(f"First line from '{file_names[0]}' and second/third lines from {len(file_names)} files appended to '{output_file}' successfully.")
    else:
        print("Error: First file is empty or does not exist.")

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: python append_lines.py <output_file> <file_name1> <file_name2> ...")
    else:
        output_file = sys.argv[1]
        file_names = sys.argv[2:]
        main(output_file, file_names)


