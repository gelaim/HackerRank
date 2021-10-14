# Enter your code here. Read input from STDIN. Print output to STDOUT
k = int(input())
l = list(map(int,input().split()))
l.sort()
for i in range(0,len(l)-k,k):

    if l[i] != l[i+k-1]:
        print(l[i])
        break
else:
    print(l[-1])

