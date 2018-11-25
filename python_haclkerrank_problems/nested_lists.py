if __name__ == '__main__':
    random =res_sort = []
    n = int(input())
    for k in range(n):
        name = input()
        score = float(input())
        random.append([name,score])
    res_sort = sorted(random)
    random.sort(key=lambda x: x[1])
    j = 0
    while (random[j][1] == random[j+1][1]):
        j = j+1
    for i in range (n):
        if random[j+1][1] == res_sort[i][1]:
            print(res_sort[i][0])
        
