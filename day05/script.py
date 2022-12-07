stacks = [
 "DLJRVGF",
 "TPMBVHJS",
 "VHMFDGPC",
 "MDPNGQ",
 "JLHNF",
 "NFVQDGTZ",
 "FDBL",
 "MJBSVDN",
 "GLD",
]

print(stacks)
with open(r"input.txt") as f:
    lines = list(map(lambda x: x.strip(),f.readlines()))
    #lines = lines[0:1]

for line in lines:
    print(line)
    commands = line.split(" ")
    amount, origin, target = int(commands[1]), int(commands[3])-1, int(commands[5])-1
    # Task 1
    #for move in range(0, amount):
    #    if len(stacks[origin] ) > 0:
    #        stacks[target] = stacks[target]+stacks[origin][-1]
    #        stacks[origin] = stacks[origin][0:-1]

    # Task 2
    if amount > len(stacks[origin]):
        stacks[target] = stacks[target]+stacks[origin]
        stacks[origin] = ""
    else:
        stacks[target] = stacks[target]+stacks[origin][-amount:]
        stacks[origin] = stacks[origin][0: -amount]


print(stacks)
