from collections import deque


def buildTree(relationships):
    tree = {}

    for relationship in relationships:
        parent = relationship[0]
        children = relationship[1:]
        tree[parent] = children

    levels = {}
    queue = deque([(0, 0)])

    while queue:
        node, level = queue.popleft()
        levels[node] = level+1

        if node in tree:
            for child in tree[node]:
                queue.append((child,level+1))

    return levels


def main():
    n = int(input().strip())
    relationships = []

    for _ in range(n):
        rel = list(map(int, input().split()))
        relationships.append(rel)

    q = int(input().strip())
    queries = [int(input()) for _ in range(q)]

    levels = buildTree(relationships)

    for i in queries:
        print(levels[i])


if __name__ == "__main__":
    main()
