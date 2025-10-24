x = int(input())
y = int(input())

is_x_positive = x > 0
is_y_positive = y > 0

if is_x_positive and is_y_positive:
    print(1)
elif is_x_positive and not is_y_positive:
    print(4)
elif not is_x_positive and is_y_positive:
    print(2)
elif not is_x_positive and not is_y_positive:
    print(3)