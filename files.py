file = open("details.txt", "a")

name = input()
age = int(input())

file.write(name + " ")
file.write(str(age) + "\n")
file.close()
