import re

def multiplyTwoNumbers(file_path):
    results =0

    with open(file_path, "r") as file:
        content = file.read()


    pattern = re.compile(r"mul\((\d{1,3}),\s*(\d{1,3})\)")

    matches = re.findall(pattern, content)

    for a, b in matches:
        results += (int(a)* int(b))


    return results

print(multiplyTwoNumbers(file_path="sample.txt"))

#go through the input
#check if the input follows this patten mul(x, y)
#if it does multiply x*y and add to a result
#return sum of the result
