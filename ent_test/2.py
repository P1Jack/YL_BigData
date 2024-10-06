from sys import stdin
from json import dump, load


lines = [line.strip() for line in stdin]
input_filename = lines[0]

with open(input_filename, 'r') as input_file:
    input_data = load(input_file)

data = {}
for i, line in enumerate(lines[1:]):
    line_type = input_data[str((i + 1) % 3)]
    data[str(i + 1)] = []
    for num in line.split(', '):
        if (int(num) % 2 and len(num) >= 3 and line_type == 'x'
                or len(set(num)) >= 3 and line_type == 'y' or line_type == 'z'):
            data[str(i + 1)].append(int(num))
    data[str(i + 1)].sort()

with open('rescue.json', 'w') as output_file:
    dump(data, output_file)
