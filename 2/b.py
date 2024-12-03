SAFE_INCERASE = [1, 2, 3]
SAFE_DECREASE = [- x for x in SAFE_INCERASE]

if __name__ == "__main__":
    with open('2\input.txt') as f:
        data = f.read().splitlines()
    
    n_safe = 0
    for report in data:
        levels = [int(x) for x in report.strip().split(" ")]
        l = len(levels)
        i = 1
        print(levels)
        while (i < l - 1 and levels[i] - levels[i - 1] in SAFE_INCERASE):
            i += 1
        if i >= l - 1:
            n_safe += 1
            continue
        elif levels[i + 1] - levels[i - 1] in SAFE_INCERASE and all(levels[j + 1] - levels[j] in SAFE_INCERASE for j in range(i + 1, l - 1)):
            n_safe += 1
            continue
        elif i > 1 and levels[i] - levels[i - 2] in SAFE_INCERASE and all(levels[j + 1] - levels[j] in SAFE_INCERASE for j in range(i, l - 1)):
            n_safe += 1
            continue
        elif i == 1 and all(levels[j + 1] - levels[j] in SAFE_INCERASE for j in range(i, l - 1)):
            n_safe += 1
            continue

        i = 1
        while (i < l - 1 and levels[i] - levels[i - 1] in SAFE_DECREASE):
            i += 1
        if i >= l - 1:
            n_safe += 1
        elif levels[i + 1] - levels[i - 1] in SAFE_DECREASE and all(levels[j + 1] - levels[j] in SAFE_DECREASE for j in range(i + 1, l - 1)):
            n_safe += 1
        elif i > 1 and levels[i] - levels[i - 2] in SAFE_DECREASE and all(levels[j + 1] - levels[j] in SAFE_DECREASE for j in range(i, l - 1)):
            n_safe += 1
        elif i == 1 and all(levels[j + 1] - levels[j] in SAFE_DECREASE for j in range(i, l - 1)):
            n_safe += 1
                
    print(n_safe)