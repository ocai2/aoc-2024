import re

if __name__ == "__main__":
    with open('3\input.txt') as f:
        data = f.read()

    pattern = r'mul\(([0-9]+,[0-9]+)\)'
    matches = re.findall(pattern, data)

    multiplications = 0
    for pair in matches:
        l, r = pair.split(',')
        multiplications += int(l) * int(r)
    
    print(multiplications)