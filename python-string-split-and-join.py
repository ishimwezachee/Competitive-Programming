def split_and_join(line):
    arr = line.split(" ")
    result = "-".join(arr)
    return result

if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)
