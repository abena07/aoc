def analyzeSafeReports(file_path):

    with  open(file_path, "r") as file:
        reports = file.read().splitlines()

    levels = []
    for item in reports:
        level = item.split(" ")
        levels.append(level)

    total_diff = []
    for level in levels:
        diff_list = []
        for index, item in enumerate(level):
           if index > 0 :
               diff =  int(level[index - 1]) - int(item)
               diff_list.append(diff)

        total_diff.append(diff_list)


    filtered_list = []
    for item in total_diff:
        strictly_decreasing = 0
        strictly_increasing = 0
        for index, j in enumerate(item):
            if j < 0 :
                strictly_decreasing += 1
            elif j > 0:
                strictly_increasing += 1

        if strictly_decreasing == len(item):
            filtered_list.append(item)

        if strictly_increasing == len(item):
            filtered_list.append(item)


    counter = 0
    for item in filtered_list:
        for index, j in enumerate(item):
            if not (1 <= abs(j) <= 3) :
                break
        else:
          counter +=1
    return counter



file_path = "part1.txt"
print(analyzeSafeReports(file_path))
