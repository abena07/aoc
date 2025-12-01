from config import INPUT_PATH

def secret_entrance(file_path):
    arr = []
    dial = 50
    count = 0
    
    with open(file_path, "r") as file:
        items = file.read().splitlines()
    
    for item in items:
        arr.append([item[0], int(item[1:])])
    #arr: [['L', 68], ['L', 30], ['R', 48], ['L', 5], ['R', 60], ['L', 55], ['L', 1], ['L', 99], ['R', 14], ['L', 82]]
    
    for key, val in arr:
        for _ in range(val):
            
            
            if key == "L":
                dial -= 1
                #dial = (dial - val) % 100
                # if dial < val:
                #     count +=1
            else:
                dial += 1
                #dial = (dial + val) % 100
                # if dial > 100:
                #     count += (dial // 100 )
                
            dial =((dial % 100) + 100) % 100
            
        
            if dial == 0:
                count +=1
                
      
    return count 
    
file_path = "input.txt"
print(secret_entrance(INPUT_PATH))
