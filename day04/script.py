with open("input.txt") as f:
    lines = f.readlines()
count = 0
for line in lines:
    sets = line.strip().split(",")
    sets = list(map(lambda x: (int(x.strip().split("-")[0]),int(x.strip().split("-")[1])), sets))
    setA = set(range(sets[0][0], sets[0][1]+1, 1))
    setB = set(range(sets[1][0], sets[1][1]+1, 1))

    # Task 1: 
    # if setA.issubset(setB) or setB.issubset(setA):
    # Task 2: 
    if len(setA.intersection(setB)) > 0:
        count = count+1
print(count)