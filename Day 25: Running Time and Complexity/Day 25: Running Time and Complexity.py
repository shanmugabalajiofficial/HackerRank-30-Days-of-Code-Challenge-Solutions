#Day 25: Running Time and Complexity


# Enter your code here. Read input from STDIN. Print output to STDOUT
import math
T= int(input())
a=[]
for i in range(T):
    n=int(input())
    a.append(n)

for i in a:
    if i == 1:
        print('Not prime')
        continue
    
    s=int(math.sqrt(i))
    flag=0
    for j in range(2, max(2, s+1)):
        if i% j==0:
            flag=1
    print('Not prime' if flag ==1 else 'Prime')
