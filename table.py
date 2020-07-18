import time

def table():
    num = int(input("Enter the number to generate table\n"))
    counter = int(input("Enter the limit\n"))
    for _i in range(1, counter + 1):
        answer = num * _i
        print(f"{num} * {_i} = {answer}")
        time.sleep(0.5)

table()
