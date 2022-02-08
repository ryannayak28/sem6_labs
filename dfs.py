def dfs(adj_list, start, target, path, visited = set()):
    path.append(start)
    visited.add(start)
    if start == target:
        return path
    for neighbour in adj_list[start]:
        if neighbour not in visited:
            result = dfs(adj_list, neighbour, target, path, visited)
            if result is not None:
                return result
    path.pop()
    return None


def main():
    adj_list = {
        0 : [1, 2, 3],  # A:[B, C, D]
        1 : [0, 4, 5],  # B:[A, E, F]
        2 : [0, 5],     # C:[A, F]
        3 : [0],        # D:[A]
        4 : [1],        # E:[B]
        5 : [1, 2]      # F:[B, C]
    }
    traversal_path = []
    traversal_path = dfs(adj_list, 0, 3, traversal_path)
    print(traversal_path)


if __name__ == "__main__":
    main()

