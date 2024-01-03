inp = input()

num = int(str([k for k, char in enumerate(inp) if char.isnumeric()]))
print(num)
