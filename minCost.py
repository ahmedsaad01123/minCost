def min_cost(matrix, m, n):
    min_cost_path = [[0 for x in range(n+1)] for y in range(m+1)]
    min_cost_path[0] = matrix[0]
    for i in range(1, n + 1):
        for j in range(0, m + 1):
            min_cost_path[i][j] = matrix[i][j] + get_up_min_cost(min_cost_path, i, j)
    return min_cost_path


def min_of_xyz(x=float('inf'), y=float('inf'), z=float('inf')):
    #print(x, y, z)
    if x < y:
        return x if (x < z) else z
    else:
        return y if (y < z) else z


def get_up_min_cost(matrix, i, j):
    #print('matrix[', i, '][', j, ']:', matrix[i][j])
    x = float('inf')
    z = float('inf')
    y = matrix[i-1][j]
    if j >= 1:
        x = matrix[i-1][j-1]
    if j < len(matrix[0])-1:
        z = matrix[i-1][j+1]
    return min_of_xyz(x, y, z)


if __name__ == '__main__':
    cost = [[10, 20, 30, 40],
            [60, 50, 20, 80],
            [20, 20, 20, 20],
            [60, 50, 20, 80]]
    m = len(cost)
    n = len(cost[0])
    min_cost_path = min_cost(cost, m-1, n-1)
    print(1000 - min(min_cost_path[n-1]))