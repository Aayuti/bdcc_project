import timeit
import platform
import sys
from collections import deque

# Breadth-First Search (BFS) Algorithm
def bfs(graph, start):
    visited = set()
    queue = deque([start])
    visited.add(start)

    while queue:
        vertex = queue.popleft()
        for neighbor in graph[vertex]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)
    return visited

# Depth-First Search (DFS) Algorithm
def dfs(graph, start):
    visited = set()
    stack = [start]

    while stack:
        vertex = stack.pop()
        if vertex not in visited:
            visited.add(vertex)
            for neighbor in graph[vertex]:
                stack.append(neighbor)
    return visited

# Minimum calculation
def calculate_min(data):
    return min(data)

# Maximum calculation
def calculate_max(data):
    return max(data)

# Range calculation
def calculate_range(data):
    return max(data) - min(data)

# Create a sample graph for testing
def create_sample_graph():
    return {
        0: [1, 2],
        1: [0, 3, 4],
        2: [0, 4],
        3: [1],
        4: [1, 2]
    }

# Compute BFS Time
def bfs_time():
    SETUP_CODE = '''
from __main__ import bfs, create_sample_graph
'''

    TEST_CODE = '''
graph = create_sample_graph()
bfs(graph, 0)'''

    # timeit.repeat statement
    times = timeit.repeat(setup=SETUP_CODE,
                          stmt=TEST_CODE,
                          repeat=3,
                          number=100)

    # Calculate and print statistics
    print('Breadth-First Search function times:')
    print('  Min Time:    {:.6f} seconds'.format(calculate_min(times)))
    print('  Max Time:    {:.6f} seconds'.format(calculate_max(times)))
    print('  Range:       {:.6f} seconds'.format(calculate_range(times)))


# Compute DFS Time
def dfs_time():
    SETUP_CODE = '''
from __main__ import dfs, create_sample_graph
'''

    TEST_CODE = '''
graph = create_sample_graph()
dfs(graph, 0)'''

    # timeit.repeat statement
    times = timeit.repeat(setup=SETUP_CODE,
                          stmt=TEST_CODE,
                          repeat=3,
                          number=100)

    # Calculate and print statistics
    print('Depth-First Search function times:')
    print('  Min Time:    {:.6f} seconds'.format(calculate_min(times)))
    print('  Max Time:    {:.6f} seconds'.format(calculate_max(times)))
    print('  Range:       {:.6f} seconds'.format(calculate_range(times)))


if __name__ == "__main__":
    dfs_time()
    bfs_time()
