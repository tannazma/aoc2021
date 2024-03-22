
# Open the file for reading
with open("inputs.txt", "r") as file:
    # Read the content of the file
    input_s = file.read()
numbers = [int(line) for line in input_s.splitlines()]

count = sum(
    numbers[i] > numbers[i - 1]
    for i in range(1, len(numbers))
) 
        
print(f"count: {count}")