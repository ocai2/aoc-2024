import re

YES = 'do'
NO = 'don\'t'

pre_ops = [YES, NO]

if __name__ == "__main__":
    with open('3\input.txt') as f:
        data = f.read()

    pattern = r'(mul|do|don\'t)\(([0-9]+,[0-9]+)*\)'
    matches = re.findall(pattern, data)

    multiplications = 0
    current_op = YES
    for match in matches:
        op, nums = match
        
        if op in pre_ops:
            current_op = op
        elif current_op == YES:
            l, r = nums.split(',')
            multiplications += int(l) * int(r)
    
    print(multiplications)