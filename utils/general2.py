def get_box_center(x):
    c1, c2 = (int(x[0]) + int(x[2])) / 2, (int(x[1]) + int(x[3])) / 2
    return int(c1), int(c2)


def check_obj_inside(input_xyxy, target_xyxy):
    x = input_xyxy
    y = target_xyxy
    if int(x[0]) > int(y[0]):
        if int(x[1]) > int(y[1]):
            if int(x[2]) < int(y[2]):
                if int(x[3]) < int(y[3]):
                    return True
    return False


def row_numeralization(row):
    value = 0
    for i, v in enumerate(reversed(row)):
        value += 10 ** i * v
    return int(value)
