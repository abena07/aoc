from config import INPUT_PATH

def is_invalid_id(num):
    s = str(num)
    length = len(s)

    if length % 2 != 0:
        return False

    midpoint = length // 2
    first_half = s[:midpoint]
    second_half = s[midpoint:]

    return first_half == second_half

def gift_shop(input_path):
    with open(input_path, "r") as file:
        contents = file.read().split(",")
    
    arr = [ content.split('-') for content in contents]
    
    res = 0
    for start, end in arr:
        for i in range(int(start), int(end)+1):
            if is_invalid_id(i):
                res += i
    return res
    
        
input_path = "input.txt"
print(gift_shop(INPUT_PATH))
            