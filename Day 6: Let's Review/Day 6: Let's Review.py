#Day 6: Let's Review


# Enter your code here. Read input from STDIN. Print output to STDOUT
if __name__ == '__main__':
    n = int(input())
    strings = [input().strip() for _ in range(n)]
    print(*[f"{string[::2]} {string[1::2]}" for string in strings], sep="\n")
