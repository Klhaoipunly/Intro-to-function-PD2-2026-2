def spaces(n, y, t):
    occupied = 0
    for i in range(n):
        if y[i] == "C" and t[i] == "C":
            occupied += 1
    return occupied



print(spaces(30, "....C.CC...CCC.C.CC..C.....CC.", "C.CC.C...C..C..C...C..C..CCC.C"))