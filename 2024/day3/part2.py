import re

def multiplySomeNumbers(file_path):
    results = 0
    flag = True

    multiply_pattern = re.compile(r"mul\((\d{1,3}),\s*(\d{1,3})\)")
    dont_pattern = re.compile(r"don't\(\)")
    do_pattern = re.compile(r"do\(\)")

    patterns = [multiply_pattern, dont_pattern, do_pattern]

    with open(file_path, "r") as file:
        content = file.read()

    combined_pattern = re.compile(r"mul\((\d{1,3}),\s*(\d{1,3})\)|don't\(\)|do\(\)")

    for match in combined_pattern.finditer(content):
        for pattern in patterns:
            if pattern.match(match.group(0)):
                if pattern == multiply_pattern:
                    if flag:
                        x = int(match.group(1))
                        y = int(match.group(2))
                        results += x * y
                elif pattern == dont_pattern:
                    flag = False
                elif pattern == do_pattern:
                    flag = True
    return results

file_path = "part2.txt"
total = multiplySomeNumbers(file_path=file_path)
print(f"Total Sum: {total}")
