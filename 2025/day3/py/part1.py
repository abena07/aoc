from config import INPUT_PATH

def lobby(input_path):
    with open(input_path, "r") as file:
        items = file.read().split()
        
    battery = 0
    
    for item in items:
        first_max = 0
        second_max = 0
        res = ""
        first_idx = 0
        
        for idx, val in enumerate(item):
            if idx != len(item)-1:
                first_max = max(first_max, int(val))
                
        first_idx =  item.index(str(first_max))
        res = str(first_max)
         
        new_num = item[first_idx+1:]    
        for idx, val in enumerate(new_num):
            second_max = max(second_max, int(val))
            
        res += str(second_max)
        battery += int(res)
    return battery      
        
      
        
input_path = "input.txt"
print(lobby(INPUT_PATH))