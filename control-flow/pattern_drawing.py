pattern = int(input("Enter the size of the pattern: "))
a = 0
while pattern > a:
    for b in range(pattern):
        print("*", end="")
    print()
    a += 1
