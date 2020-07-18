import time

num = 2
counter = 0
while True:
    answer = num ** counter
    counter += 1
    print(f"{num} ^ {counter} = {answer}")
    time.sleep(0.5)
