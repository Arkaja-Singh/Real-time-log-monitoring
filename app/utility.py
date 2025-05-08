# app/utility.py

def read_new_lines(file):
    lines = []
    while True:
        line = file.readline()
        if not line:
            break
        lines.append(line)
    return lines
