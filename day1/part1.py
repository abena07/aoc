def totalDistanceBetweenList(file_path):
    list1 =[]
    list2 = []
    with open(file_path, "r") as file:
        words = file.read().splitlines()

    for word in words:
        left, right = word.split("   ")
        list1.append(int(left))
        list2.append(int(right))

    sorted_list1 = sorted(list1)
    sorted_list2 = sorted(list2)

    total_diff = 0

    for a, b in zip(sorted_list1, sorted_list2):
        total_diff += abs(a-b)
    return total_diff

file_path = "part1.txt"
print(totalDistanceBetweenList(file_path))
