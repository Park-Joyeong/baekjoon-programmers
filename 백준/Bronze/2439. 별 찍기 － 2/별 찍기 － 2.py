no = int(input())
for i in range(no):
    for j in range(no):
        if j <= no-2-i:
            print(" ", end="")
        else:
            print("*", end="")
    print()