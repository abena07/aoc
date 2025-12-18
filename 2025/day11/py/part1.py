from collections import defaultdict

def reactor(input_path):
    with open(input_path) as file:
        items = file.read().splitlines()

        cache = defaultdict(list)
        for item in items:
            cache[item[0:3]].extend(item[5:].split())
    
        path = 0
        def dfs(val):
            nonlocal path

            #base case
            if val == 'out':
                path += 1
                return
            
            #recursive case
            for item in cache[val]:
                dfs(item)

        if 'you' in cache:
            for val in cache['you']:
                dfs(val)
            return path

print(reactor("../input.txt"))















