from collections import defaultdict
def findSimilarityScore(file_path):
    list1 =[]
    list2 = []
    with open(file_path, "r") as file:
        words = file.read().splitlines()

    for word in words:
        left, right = word.split("   ")
        list1.append(int(left))
        list2.append(int(right))


    counter = defaultdict(int)

    for num in list2:
        counter[num] +=1

    similarity = 0
    for num in list1:
        if num in counter:
            similarity += num *counter[num]
    return similarity

file_path = "part2.txt"
print(findSimilarityScore(file_path))
