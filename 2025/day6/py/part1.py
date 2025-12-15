import math

def trash_compactor(input_path):
    with open(input_path) as file:
        rows = [line.split() for line in file]

    # transpose rows → columns
    columns = list(zip(*rows))
    total = 0
    # join each column
    for col in columns:
        nums = []
        operator = []
        res1 = 0
        res2 = 0
        
        for item in col:
            if item.isdigit():
                nums.append(int(item))
            else:
                operator.append(item)

        if operator[-1] == '+':
            res1 += sum(nums)
        else:
            res2 += math.prod(nums)

        total += res1
        total += res2
    
    return total



    print("rows", rows)
    print("columns", columns)


print(trash_compactor("../input.txt"))
