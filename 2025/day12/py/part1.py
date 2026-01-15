def parse_input(lines):
    shapes = {}
    regions = []

    i = 0
    n = len(lines)
    while i < n:
        line = lines[i].strip()
        if not line:
            i += 1
            continue

        # Shape definition: "0:", "1:", etc.
        if line.endswith(':') and all(c.isdigit() for c in line[:-1]):
            shape_id = int(line[:-1])
            i += 1
            shape = []
            while i < n and lines[i].strip():
                shape.append(lines[i].strip())
                i += 1
            shapes[shape_id] = shape

        # Region definition: "WxH: counts"
        elif 'x' in line and ':' in line:
            dims_part, counts_part = line.split(':', 1)
            width, height = map(int, dims_part.split('x'))
            counts = list(map(int, counts_part.split()))
            regions.append((width, height, counts))
            i += 1
        else:
            i += 1

    return shapes, regions


def solve(input_path):
    with open(input_path) as f:
        lines = f.readlines()

    shapes, regions = parse_input(lines)
    packable_count = 0

    for width, height, present_counts in regions:
        num_presents = sum(present_counts)
        # Each present occupies 8 cells (3x3 minus 1 gap)
        if num_presents * 8 <= width * height:
            packable_count += 1

    return packable_count


print(solve("../input.txt"))
