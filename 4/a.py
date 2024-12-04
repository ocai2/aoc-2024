import numpy as np

MATCH = 'XMAS'
MATCH_REVERSED = MATCH[::-1]

def get_matches(s):
    return s.count(MATCH) + s.count(MATCH_REVERSED)

if __name__ == "__main__":
    with open('4\input.txt') as f:
        li = [[ch for ch in line] for line in f.read().splitlines()]
    
    arr = np.array(li)
    l = len(arr)

    n_matches = 0
    for i in range(l):
        s = "".join(arr[i])
        n_matches += get_matches(s)

        s = "".join(arr[:,i])
        n_matches += get_matches(s)

        s = "".join(arr.diagonal(i))
        n_matches += get_matches(s)

        s = "".join(np.fliplr(arr).diagonal(i))
        n_matches += get_matches(s)

        if i != 0:
            s = "".join(arr.diagonal(-i))
            n_matches += get_matches(s)

            s = "".join(np.fliplr(arr).diagonal(-i))
            n_matches += get_matches(s)
        
    print(n_matches)