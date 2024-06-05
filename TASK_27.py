with open('DATA/27A (1).txt') as f:
    n = int(f.readline())
    k = int(f.readline())
    d = [(index, int(num)) for index, num in enumerate(f)]
    
