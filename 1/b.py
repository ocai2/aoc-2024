from collections import Counter

if __name__ == "__main__":
    with open('1\input.txt') as f:
        data = [[int(x) for x in line.split("   ")] for line in f.read().splitlines()]
        l, r = map(list, zip(*data))
        l.sort(), r.sort()
    
    occurances = Counter(r)
    similarity = 0
    for i, x in enumerate(l):
        similarity += 0 if x not in occurances else occurances[x] * x
    
    print(similarity)