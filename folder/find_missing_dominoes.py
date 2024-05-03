def find_missing_dominoes(available_dominoes, used_dominoes):
    all_dominoes = set(map(tuple, available_dominoes))
    used_dominoes = set(map(tuple, used_dominoes))
    missing_dominoes = all_dominoes.difference(used_dominoes)
    return sorted(list(map(list, missing_dominoes)))


available_dominoes = [[0, 0], [0, 1], [0, 2], [0, 3],
                      [0, 4], [0, 5], [0, 6], [1, 1],
                      [1, 2], [1, 3], [1, 4], [1, 5],
                      [1, 6], [2, 2], [2, 3], [2, 4],
                      [2, 5], [2, 6], [3, 3], [3, 4],
                      [3, 5], [3, 6], [4, 4], [4, 5],
                      [4, 6], [5, 5], [5, 6], [6, 6]]
used_dominoes = [[1, 6], [5, 1], [4, 5], [5, 5], [2, 6], [6, 0], [0, 1]]
missing_dominoes = find_missing_dominoes(available_dominoes, used_dominoes)

print("Missing dominoes:", missing_dominoes)
