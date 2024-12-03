SAFE_INCERASE = [1, 2, 3]
SAFE_DECREASE = [- x for x in SAFE_INCERASE]

if __name__ == "__main__":
    with open('2\input.txt') as f:
        data = f.read().splitlines()
    
    n_safe = 0
    for report in data:
        levels = [int(x) for x in report.strip().split(" ")]
        if all(levels[i + 1] - levels[i] in SAFE_INCERASE for i in range(len(levels) - 1)):
            n_safe += 1
        elif all(levels[i + 1] - levels[i] in SAFE_DECREASE for i in range(len(levels) - 1)):
            n_safe += 1
    
    print(n_safe)