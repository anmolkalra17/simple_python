import math
int1 = int(input())
int2 = int(input())

if int1 > int2:
    if int2 < 0 or 0 < int2 < 1:
        log = math.log(int2)
        print(round(log, 2))
    else:
        log = math.log(int1, int2)
        print(round(log, 2))
