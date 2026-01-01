from math import dist, prod

def solve(puzzle_input):
   
    # -------------------------
    # 1. Read the input
    # -------------------------
    # Each line in the input file represents a junction box as 3D coordinates (x, y, z)
    with open(puzzle_input) as file:
        junctions = [
            tuple(map(int, line.split(",")))
            for line in file
        ]
    n = len(junctions)
    print(f"{junctions=}")

    # -------------------------
    # 2. Union-Find setup
    # -------------------------
    # 'parent' keeps track of the representative of each circuit
    # 'size' stores the number of junction boxes in each circuit
    parent = list(range(n))
    size = [1] * n  # initially, each junction is its own circuit

    # -------------------------
    # 2a. Find function with path compression
    # -------------------------
    # Returns the root parent of a junction box, and flattens the tree for efficiency
    def find(x):
        if parent[x] != x:
            parent[x] = find(parent[x])
        return parent[x]
    
    # -------------------------
    # 2b. Union function with union by size
    # -------------------------
    # Connects two junctions into the same circuit
    def union(a, b):
        ra = find(a)
        rb = find(b)

        if ra == rb:
            return  # already in the same circuit, do nothing

        # Attach the smaller circuit to the larger one
        if size[ra] < size[rb]:
            ra, rb = rb, ra

        parent[rb] = ra
        size[ra] += size[rb]

    # -------------------------
    # 3. Compute all pairwise distances
    # -------------------------
    # For each pair of junction boxes, compute the straight-line distance between them
    distances = []
    for i in range(n - 1):
        for j in range(i + 1, n):
            d = dist(junctions[i], junctions[j])
            distances.append((d, i, j))

    # -------------------------
    # 4. Sort distances and connect the closest pairs
    # -------------------------
    # Only the first 1000 shortest connections are made (as per puzzle instructions)
    distances.sort(key=lambda x: x[0])
    for _, i, j in distances[:1000]:
        union(i, j)

    # -------------------------
    # 5. Collect sizes of all circuits
    # -------------------------
    # Map each root to its circuit size
    circuits = {}
    for i in range(n):
        root = find(i)
        circuits[root] = size[root]

    print(f"\n{circuits=}")

    # -------------------------
    # 6. Compute the final answer
    # -------------------------
    # Multiply the sizes of the three largest circuits
    largest_three = sorted(circuits.values())[-3:]
    print(f"\n{largest_three=}")
    
    return prod(largest_three)


print(solve("../sample.txt"))
