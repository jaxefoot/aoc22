with open("input.txt") as f:
    signal = f.readline()

#Task1
#markerSize = 4

#Task 2
markerSize = 14

for i in range(0, len(signal)+1):
    if i > markerSize and len(set(signal[i-markerSize:i])) == markerSize:
        print(signal[:i])
        print(len(signal[:i]))
        break