t = int(input())
for i in range(t):
    x,y,k = map(int,input().split())
    total = (x+y)//k
    
    if total%2==0:
        print("Chef")
    else:
        print("Paja")
