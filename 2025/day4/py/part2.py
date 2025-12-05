def printing_department(input_path):
    with open(input_path, "r") as file:
        items = file.read().split()

    matrix = [list(item) for item in items]
    
    nrows = len(matrix)
    ncols = len(matrix[0])
    total = 0
    
    while True:
        res = 0   
        for r in range(nrows):
            for c in range(ncols):
                if matrix[r][c] == "@": 
                    dirs = [
                            (0,1), (0,-1), (1, 0), (-1,0),
                            (-1,-1), (-1,1), (1, -1), (1,1)    
                    ]
                    count = 0
                        
                    for dr, dc in dirs:
                        nr = r + dr
                        nc = c + dc
                        if 0 <= nr < nrows and 0 <= nc < ncols and matrix[nr][nc] == "@": 
                            count += 1
                                
                                    
                    if count < 4:
                        res +=1
                        print("res", res)
                        matrix[r][c] = "x"
                        
        if res == 0:
            break
        total += res
    return total
                    

input_path = "input.txt"
print(printing_department("../input.txt"))