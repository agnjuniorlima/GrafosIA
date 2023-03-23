from collections import defaultdict

def dominating_set(graph, start):
    visited = set()
    queue = [start]
    while queue:
        node = queue.pop(0)
        visited.add(node)
        for neighbor in graph[node]:
            if neighbor not in visited:
                queue.append(neighbor)
    return visited

# Example usage
graph = defaultdict(list)
graph[1] = [0,1]
graph[2] = [0,2]
graph[3] = [0,3]
graph[4] = [1,3]
graph[5] = [2,3]
graph[6] = [3,4]
graph[7] = [4,6]
graph[8] = [5,6]


print(dominating_set(graph, 8))