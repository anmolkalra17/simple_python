num = int(input("Enter a number \n"))
total = 0
while num != 0:
    rem = int(num) % 10
    total += rem
    num /= 10
print("sum = ",total)
