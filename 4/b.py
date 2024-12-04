import numpy as np

MATCHES = ['MMASS','SSAMM','MSAMS', 'SMASM']

if __name__ == "__main__":
    with open('4\input.txt') as f:
        li = [[ch for ch in line] for line in f.read().splitlines()]
    
    arr = np.array(li)
    l = len(arr)

    n_matches = 0
    for i in range(l - 2):
        for j in range(l - 2):
            s = "".join([arr[i,j], arr[i+2,j], arr[i+1,j+1], arr[i,j+2], arr[i+2,j+2]])
            if s in MATCHES: n_matches += 1

    print(n_matches)