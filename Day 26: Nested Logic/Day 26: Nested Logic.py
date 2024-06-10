#Day 26: Nested Logic


# Enter your code here. Read input from STDIN. Print output to STDOUT
d1, m1, y1=map(int, input().split())
d2, m2, y2=map(int, input().split())
if y1<y2 or (y1==y2 and m1<m2) or (y1==y2 and m1==m2 and d1<=d2):
    print(0)
elif y1==y2 and m1==m2:
    print(15 * (d1-d2))
elif y1==y2:
    print(500 * (m1-m2))
else:
    print(10000)
