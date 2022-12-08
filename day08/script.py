with open("input.txt") as f:
    lines = f.readlines()
    lines = list(map(lambda x: x.strip(), lines))
    

checkVerticalVisibility(1, 1, lines)

def checkVerticalVisibility(x, y, lines):
    if y == 0 or y == len(lines-1):
        return True
    