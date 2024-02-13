if __name__ == '__main__':
    names = []
    scores = []
    score_name = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        score_name.append([name,score])
        scores.append(score)
    
    result = sorted(list(set(scores)))
    second_small = result[1]
    
    for item in score_name:
        if item[1] == second_small:
            names.append(item[0])
    for name in sorted(names):
        print(name)
        
