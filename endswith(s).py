word = input().split()
ending_with_s = []
for i in word:
    if i.endswith("s"):
        ending_with_s.append(i)

print(*ending_with_s, sep="_")

