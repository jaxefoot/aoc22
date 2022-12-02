def getOption(opponent, goal):
    options = ["A", "B", "C"]
    if goal == "Y":
        return opponent
    elif goal == "X":
        return options[ord(opponent) - 65 - 1]
    elif goal == "Z":
        return options[(ord(opponent) - 65 + 1) % 3]

def calculateRoundPoints(me, opponent):
    roundPoints = 0
    roundPoints += ord(me) - 64
    if (ord(me) - ord(opponent)) == 1 or (ord(me) - ord(opponent)) == -2:
        roundPoints += 6
    elif (ord(me) - ord(opponent)) == 0:
        roundPoints += 3
    return roundPoints

# Task 1
with open("input.txt") as f:
    lines = f.readlines()
myPoints = 0
for line in lines:

    opponent = line[0]
    me = chr(ord(line[2]) - 23)
    myPoints += calculateRoundPoints(me, opponent)
print("Task 1", myPoints)

# Task 2
with open("input.txt") as f:
    lines = f.readlines()
myPoints = 0
for line in lines:
    opponent = line[0]
    me = getOption(opponent, line[2])
    myPoints += calculateRoundPoints(me, opponent)
print("Task 2", myPoints)
