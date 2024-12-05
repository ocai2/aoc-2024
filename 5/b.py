def index_no_value_error(c, l):
    try:
        return l.index(c)
    except ValueError:
        return -1


if __name__ == "__main__":
    with open('5\input.txt') as f:
        data = f.read().split('\n\n')
        rules_raw = data[0].splitlines()
        updates = data[1].splitlines()
    

    rules = {}
    for r in rules_raw:
        nums = r.split('|')
        if nums[1] not in rules:
            rules[nums[1]] = [nums[0]]
        else:
            rules[nums[1]].append(nums[0])

    result = 0
    for u in updates:
        line =  u.split(',')
        accept = False
        changed = True
        while changed:
            changed = False
            for i, n in enumerate(line):
                swap = i
                if n in rules:
                    for c in rules[n]:
                        if (x:= index_no_value_error(c, line)) > swap:
                            swap = x
                            accept = True
                            changed = True
                line[i], line[swap] = line[swap], line[i]

        if accept:
            result += int(line[len(line) // 2])
    
    print(result)
