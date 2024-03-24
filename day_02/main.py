# Open the file for reading
with open("inputs.txt", "r") as file:    
    numbers = [x for x  in file.read().split("\n")]

x = 0
y = 0
for xInData in numbers:
    xInData = xInData.split()
    # xInData has 2 values inside [0] is forward or down and [1] is a number should be convert to int
    if xInData[0] == "forward":
        x += int(xInData[1])
    elif xInData[0]== "down":
        y += int(xInData[1])
    else :
        y -= int(xInData[1])
        
print(xInData, xInData[1], x, y, x*y)