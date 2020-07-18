old_list = [int(num) for num in input().split()]

binary_list = []
for num in old_list:
    if num > 0:
        num = 1
        binary_list.append(num)
    else:
        num = 0
        binary_list.append(num)

print(binary_list)
