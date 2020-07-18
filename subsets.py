import itertools  
def findsubsets(s, n): 
    return [set(i) for i in itertools.combinations(s, n)] 

n = int(input("Enter size"))
s = set()

print("Enter set")

while n != 0:
    s.add(int(input))
    n -= 1

print(findsubsets(s, n))
