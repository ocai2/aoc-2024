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
        compliant = True
        line =  u.split(',')
        for i, n in enumerate(line):
            if n in rules:
                if not all(c not in line[i:] for c in rules[n]):
                    compliant = False
                    break

        if compliant:
            result += int(line[len(line) // 2])
    
    print(result)
