def cafeteria(input_path):
    with open(input_path, "r") as file:
        items = file.read().split()
        
        intervals = [item.split("-") for item in items if "-" in item ]
        integers = [int(item) for item in items if "-" not in item ]
          
        new_intervals = [[int(a), int(b)] for a, b in intervals]
        new_intervals.sort(key = lambda x : x[0])
        output = [new_intervals[0]]
     
        for start, end in new_intervals[1:]:
            if int(output[-1][1]) >= int(start):
                output[-1][1] = max(output[-1][1], end)
            else:
                output.append([start, end])
        
        fresh = 0
        
        for start, end in output:
            for integer in integers:
                if start <= integer <= end:
                    fresh += 1
        
        return fresh
                            
print(cafeteria("../input.txt"))

 
 
 
 
 

    