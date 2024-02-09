if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    
    val = list(set(sorted(list(arr))))
    print(val[-2])
