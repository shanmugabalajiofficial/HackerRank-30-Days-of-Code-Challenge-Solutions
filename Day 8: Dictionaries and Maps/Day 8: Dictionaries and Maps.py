#Day 8: Dictionaries and Maps


# Enter your code here. Read input from STDIN. Print output to STDOUT
try:
    n = int(input())
    phoneBook = {}
    
    # Input phone book entries
    for i in range(n):
        key, value = input().split()
        phoneBook[key] = value
    
    # Query phone book
    while True:
        try:
            name = input()
            if not name:  # Check for empty input, exit loop if encountered
                break
            if name in phoneBook:
                print(name + '=' + phoneBook[name])
            else:
                print('Not found')
        except EOFError:  # Handle end of input
            break

except Exception as e:
    print("Error:", e)
