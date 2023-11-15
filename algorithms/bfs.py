import collections


def bfs(graph, root):
    visited = set()
    queue = collections.deque([root])

    while queue:
        vertex = queue.popleft()
        visited.add(vertex)
        for i in graph[vertex]:
            if i not in visited:
                queue.append(i)

    print(visited)


if __name__ == "__main__":
    graph = {
        "A": ["B", "C", "D"],
        "B": ["A", "E", "F"],
        "C": ["A", "G"],
        "D": ["A", "H", "I"],
        "E": ["B"],
        "F": ["B"],
        "G": ["C"],
        "H": ["D"],
        "I": ["D"],
    }
    bfs(graph, "A")
