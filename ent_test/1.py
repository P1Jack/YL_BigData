with open('yl_bd/input.txt', 'r') as input_f:
    lines = input_f.readlines()
sample = lines[0][:4]
input_lines = lines[1:]
for line in input_lines:
    if sample in line.split():
        with open('yl_bd/output.txt', 'a') as output_f:
            output_f.write(line)
