#Day 8: Dictionaries and Maps


# Enter your code here. Read input from STDIN. Print output to STDOUT
n = int(input())
phoneBook = {}
for i in range(0, n):
    key, value = input().split()
    phoneBook[key]=value
for i in range(0, n):
    name = input()
    if name in phoneBook:
        print(name +'=' + phoneBook[name])
    else:
        print('Not found')
