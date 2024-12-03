if __name__ == "__main__":
    with open('1\input.txt') as f:
        data = [[int(x) for x in line.split("   ")] for line in f.read().splitlines()]
        l, r = map(list, zip(*data))
        l.sort(), r.sort()

    distance = 0
    for i, _ in enumerate(l):
        distance += abs(l[i] - r[i])
    
    print(distance)