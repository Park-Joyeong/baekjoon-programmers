no1, no2, no3 = input().split()
no1 = int(no1)
no2 = int(no2)
no3 = int(no3)

is_3_match = (no1 == no2 and no2 == no3)
is_2_match = (
    (no1 == no2 and no1 != no3 and no2 != no3) 
    or (no1 != no2 and no1 == no3 and no2 != no3)
    or (no1 != no2 and no1 != no3 and no2 == no3)
)
is_1_match = (no1 != no2 and no1 != no3 and no2 != no3)

if is_3_match:
    print(10000 + no1 * 1000)
elif is_2_match:
    if no1 == no2 or no1 == no3:
        print(1000 + no1 * 100)
    elif no2 == no3:
        print(1000 + no2 * 100)
elif is_1_match:
    if no1 > no2 and no1 > no3:
        print(no1 * 100)
    elif no2 > no1 and no2 > no3:
        print(no2 * 100)
    elif no3 > no1 and no3 > no2:
        print(no3 * 100)