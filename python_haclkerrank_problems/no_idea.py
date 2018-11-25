list = input().split()
n = int(list[0])
m = int(list[1])
l = map(int,input().split())
arr1 = map(int,input().split())
arr1 = set(arr1)
arr2 = map(int,input().split())
arr2 = set(arr2)
ans = 0
for inp in l:
    if inp in arr1:
        ans = ans + 1
    if inp in arr2:
        ans = ans - 1
print(ans)
