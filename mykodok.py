def spiral(n):
    dx, dy = 0, 1
    x, y = 0, 0
    matrix = [[' ' for _ in range(n)] for _ in range(n)]

    for i in range(1, n * n + 1):
        matrix[x][y] = '*'
        nx, ny = x + dx, y + dy
        if 0 <= nx < n and 0 <= ny < n and matrix[nx][ny] == ' ':
            x, y = nx, ny
        else:
            dx, dy = -dy, dx
            x, y = x + dx, y + dy

    for row in matrix:
        print(' '.join(row))

n = 12  # Ganti n sesuai dengan ukuran spiral yang Anda inginkan
spiral(n)
