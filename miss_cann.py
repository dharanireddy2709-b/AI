from collections import deque

# Possible boat moves (M, C)
MOVES = [(1,0),(2,0),(0,1),(0,2),(1,1)]

class Node:
    def __init__(self, state, parent=None):
        self.state = state
        self.parent = parent

    def path(self):
        node = self
        result = []
        while node:
            result.append(node.state)
            node = node.parent
        return result[::-1]


def is_valid(state):
    M, C, boat = state
    M_right = 3 - M
    C_right = 3 - C

    if M < 0 or C < 0 or M > 3 or C > 3:
        return False
    if M > 0 and C > M:
        return False
    if M_right > 0 and C_right > M_right:
        return False
    return True


def successors(state):
    M, C, boat = state
    next_states = []

    for m, c in MOVES:
        if boat == 0:
            new_state = (M - m, C - c, 1)
        else:
            new_state = (M + m, C + c, 0)

        if is_valid(new_state):
            next_states.append(new_state)

    return next_states
def bfs(start, goal):
    queue = deque([Node(start)])
    visited = set()

    while queue:
        node = queue.popleft()
        if node.state == goal:
            return node.path()

        visited.add(node.state)

        for s in successors(node.state):
            if s not in visited:
                queue.append(Node(s, node))
    return None
def dfs(start, goal):
    stack = [Node(start)]
    visited = set()

    while stack:
        node = stack.pop()
        if node.state == goal:
            return node.path()

        visited.add(node.state)

        for s in successors(node.state):
            if s not in visited:
                stack.append(Node(s, node))
    return None
def dls(node, goal, limit):
    if node.state == goal:
        return node.path()
    if limit <= 0:
        return None

    for s in successors(node.state):
        child = Node(s, node)
        result = dls(child, goal, limit - 1)
        if result:
            return result
    return None
def iddfs(start, goal):
    depth = 0
    while True:
        result = dls(Node(start), goal, depth)
        if result:
            return result
        depth += 1
start = (3,3,0)
goal = (0,0,1)

print("BFS Solution:")
print(bfs(start, goal))

print("\nDFS Solution:")
print(dfs(start, goal))

print("\nIDDFS Solution:")
print(iddfs(start, goal))
