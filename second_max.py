n = int(input())

arr=list(map(int,input().split()))
m1 =max(arr)
for i in range(n):
    if m1 == max(arr):
        arr.remove(m1)

m2 = max(arr)
print(m2)

