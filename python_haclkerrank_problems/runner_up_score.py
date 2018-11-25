if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    maxi = max(arr)
    mini = 0
    for i in range(0,n):
        if(arr[i] < maxi):
            if(arr[i] >= 0 and arr[i] > mini):
                mini = arr[i]
            elif(arr[i] < 0 and mini == 0):
                mini = arr[i]
    print(mini)
            
