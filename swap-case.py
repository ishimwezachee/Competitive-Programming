def change(letter):
    if letter.isupper():
        return letter.lower()
    else:
        return letter.upper()

def swap_case(s):
    result = ''
    for letter in s:
        result += change(letter)
    return result

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)
