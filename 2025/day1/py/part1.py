from config import INPUT_PATH

def secret_entrance(file_path):
    arr = []
    dial = 50
    count = 0
    
    with open(file_path, "r") as file:
        items = file.read().splitlines()
    
    for item in items:
        arr.append([item[0], int(item[1:])])
        
    for idx, val in arr:
        if idx == "L":
            dial = (dial - val) % 100
        else:
            dial = (dial + val) % 100
            
        if dial == 0:
            count +=1
    return count 
    
file_path = "part1.txt"
print(secret_entrance(INPUT_PATH))
            
        
        