name = input("Enter your name\n")
file = open("details.txt", "r")
text = file.read()
if name in text:
    for i in text:
        if text.has(" "):
            age = text[:i]
    print(f"Your age is {age} years.")
file.close()
