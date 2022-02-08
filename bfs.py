from queue import Queue

def bfs(adj_list, start_node, target_node):
    # Set of visited nodes to prevent loops
    visited = set()
    queue = Queue()

    # Add the start_node to the queue and visited list
    queue.put(start_node)
    visited.add(start_node)

    # start_node has not parents
    parent = dict()
    parent[start_node] = None

    # Perform step 3
    path_found = False
    while not queue.empty():
        current_node = queue.get()
        if current_node == target_node:
            path_found = True
            break

        for next_node in adj_list[current_node]:
            if next_node not in visited:
                queue.put(next_node)
                parent[next_node] = current_node
                visited.add(next_node)

    # Path reconstruction
    path = []
    if path_found:
        path.append(target_node)
        while parent[target_node] is not None:
            path.append(parent[target_node])
            target_node = parent[target_node]
        path.reverse()
    return path


def main():
    graph = {
        0 : [1, 2, 3],  # A:[B, C, D]
        1 : [0, 4, 5],  # B:[A, E, F]
        2 : [0, 5],     # C:[A, F]
        3 : [0],        # D:[A]
        4 : [1],        # E:[B]
        5 : [1, 2]      # F:[B, C]
    }
    print(bfs(graph, 0, 3))

if __name__ == "__main__":
    main()

