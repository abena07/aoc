def movie_theater(input_path):
    
    with open(input_path) as file:
        items = file.read().split()
        
        cells = [item.split(",") for item in items]
     
        max_area = 0
        
        for i in range(len(cells)):
            for j in range(1, len(cells)):
                x1, y1 = map(int, cells[i])
                x2, y2 = map(int, cells[j])
                width = abs(x2-x1) + 1
                height = abs(y2-y1) + 1
                area = width * height
                max_area = max(max_area, area)
                
        return max_area
   
print(movie_theater("../input.txt"))