import numpy as np

def getScore(item):
    asciiCode = ord(item)
    if ord("a")<= asciiCode <= ord("z"):
        return asciiCode-96
    elif ord("A") <= asciiCode <= ord("Z"):
        return asciiCode-38
    return 0

with open("input.txt") as f:
    lines = f.readlines()
    lines = lines[0:]
#Task 1
commonItems = []
for line in lines:
    line = line.strip()
    compartment1 = line[0:int(len(line)/2)]
    compartment2 = line[int(len(line)/2):len(line)]
    compartments = [compartment1, compartment2]
    intersection = next(iter(set.intersection(*[set(list) for list in compartments])))
    commonItems += intersection
points = list(map(lambda x: getScore(x), commonItems))
print("Task 1", sum(points))

#Task 2
commonItems = []
groups = np.split(np.asarray(lines), int(len(lines)/3))
for group in groups:
    vfunc = np.vectorize(lambda x: x.strip())
    group = vfunc(group)
    intersection = next(iter(set.intersection(*[set(list) for list in group])))
    commonItems += intersection
points = list(map(lambda x: getScore(x), commonItems))
print("Task 2", sum(points))