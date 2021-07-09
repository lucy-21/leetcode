"""
DFS (깊이 우선 탐색)
- 사용 : 백트래킹
- 구현 : 스택 또는 재귀

BFS (너비 우선 탐색)
- 사용 : 최단 경로 찾는 다익스트라 알고리즘 등
- 구현 : 큐 (재귀 X - 불가능!)

참고) 백트래킹
- 해결책에 대한 후보를 구축해 나아가다, 가능성이 없다고 판단되는 즉시 후보를 포기해 정답을 찾아가는 범용적인 알고리즘
- DFS와 같은 방식으로 탐색하는 모든 방법을 뜻함
- 구현 : 재귀
"""

# 샘플 그래프
graph = {
    1: [2, 3, 4],
    2: [5],
    3: [5],
    4: [],
    5: [6, 7],
    6: [],
    7: [3],
}

# 재귀를 이용한 DFS
def recursive_dfs(v, discovered=[]):
    discovered.append(v)
    for w in graph[v]:
        if w not in discovered:
            recursive_dfs(w, discovered)
    return discovered


# 스택을 이용한 DFS
def iterative_dfs(start_v):
    discovered = []
    stack = [start_v]
    while stack:
        v = stack.pop()
        if v not in discovered:
            discovered.append(v)
            for w in graph[v]:
                stack.append(w)
    return discovered


# 큐를 이용한 BFS
def iterative_bfs(start_v):
    discovered = [start_v]
    queue = [start_v]
    while queue:
        v = queue.pop(0)
        for w in graph[v]:
            if w not in discovered:
                discovered.append(w)
                queue.append(w)
    return discovered


if __name__ == "__main__":
    print("Recursive DFS: " + str(recursive_dfs(1)))
    print("Stack DFS: " + str(iterative_dfs(1)))
    print("Queue BFS: " + str(iterative_bfs(1)))
