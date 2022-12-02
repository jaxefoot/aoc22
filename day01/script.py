import numpy as np

with open(r"./input.txt") as f:
    lines = f.read().splitlines()
    lines = [";" if len(line) is 0 else line for line in lines]
    lines = " ".join(map(str,lines))
    lines = lines.split(" ; ")
    result=[]
    for line in lines:
        values = line.split(" ")
        values = (int(value) for value in values)
        result.append(sum(values))

argmax = np.max(result)
print(argmax)


print("Rätsel 2")
result.sort(reverse=True)
print(sum(result[0:3]))