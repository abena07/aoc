from collections import deque

def bfs_min_presses(buttons, target):
    start = 0
    queue = deque([(start, 0)])
    visited = {start}

    while queue:
        state, dist = queue.popleft()
        if state == target:
            return dist

        for b in buttons:
            nxt = state ^ b
            if nxt not in visited:
                visited.add(nxt)
                queue.append((nxt, dist + 1))

    return -1  # Return -1 if target is unreachable

def solve(filename):
    total_presses = 0
    
    with open(filename) as file:
        for line_num, line in enumerate(file, 1):
            line = line.strip()
            if not line:
                continue

            # Split by spaces
            parts = line.split()
            
            # Parse target (first element in square brackets)
            target_str = parts[0]
            
            # Extract buttons (elements in parentheses)
            buttons = []
            for part in parts[1:]:
                if part.startswith('{'):
                    break
                if part.startswith('('):
                    buttons.append(part)
            
            # Parse target into binary integer
            # Create bit pattern where bit i corresponds to light i
            target_int = 0
            
            for i, symb in enumerate(target_str.strip("[]")):
                if symb == "#":
                    target_int |= (1 << i)
            
            print(f"Machine {line_num}: {target_str}")
            print(f"Target state: {target_int} (binary: {bin(target_int)})")

            # Process each button tuple
            buttons_list = []
            for button in buttons:
                # Create bit pattern for this button
                button_int = 0
                
                # Remove parentheses and split by comma
                nums = button.strip("()").split(",")
                for n in nums:
                    if n:  # skip empty
                        idx = int(n)
                        button_int |= (1 << idx)
                
                buttons_list.append(button_int)
                print(f"  Button {button}: {button_int} (binary: {bin(button_int)})")

            # Run BFS to find minimum presses
            result = bfs_min_presses(buttons_list, target_int)
            
            if result == -1:
                print(f"  Result: Target unreachable")
            else:
                print(f"  Result: Minimum presses = {result}")
                total_presses += result
            
            print()
    
    print(f"Total button presses required: {total_presses}")
    return total_presses

# Example usage
if __name__ == "__main__":
    solve("../sample.txt")