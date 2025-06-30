import time
import random

def max_capsulas_array_con_camino(grid):
    n = len(grid)
    dp = [[[-1] * (2 * n) for _ in range(n)] for _ in range(n)]
    camino_dp = [[[""] * (2 * n) for _ in range(n)] for _ in range(n)]

    movimientos = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # arriba, abajo, izquierda, derecha

    def f(x, y, t):
        if x < 0 or x >= n or y < 0 or y >= n or t >= 2 * n:
            return float('-inf'), []

        if grid[x][y] == 'B':
            return float('-inf'), []

        if x == n - 1 and y == n - 1:
            valor = 1 if grid[x][y] == 'R' else 0
            return valor, [(x, y)]

        if dp[x][y][t] != -1:
            return dp[x][y][t], camino_dp[x][y][t]

        # recolectamos si es R y no ha sido recolectada (marcar como . para llamadas hijas)
        valor_actual = 1 if grid[x][y] == 'R' else 0
        original = grid[x][y]
        if original == 'R':
            grid[x][y] = '.'

        mejor_valor = float('-inf')
        mejor_camino = []

        for dx, dy in movimientos:
            nx, ny = x + dx, y + dy
            resultado, camino = f(nx, ny, t + 1)
            if resultado > mejor_valor:
                mejor_valor = resultado
                mejor_camino = camino

        total_valor = valor_actual + mejor_valor
        camino_completo = [(x, y)] + mejor_camino

        dp[x][y][t] = total_valor
        camino_dp[x][y][t] = camino_completo

        # restauramos si era R para que otras ramas lo vean
        grid[x][y] = original

        return total_valor, camino_completo

    total, camino = f(0, 0, 0)

    return total, camino

def generar_grid(n):
    opciones = ['.', '.', '.', '.', 'B', 'R']
    return [[random.choice(opciones) for _ in range(n)] for _ in range(n)]


""" n = 10
grid = generar_grid(n)

for fila in grid:
    print(fila) 

inicio = time.time()
total, camino = max_capsulas_array_con_camino(grid)
fin = time.time()

print(f"Array - n={n}: {fin - inicio:.4f} s")

print(total)
print(camino)     """
n= 3
dp = [[[-1] * (2 * n) for _ in range(n)] for _ in range(n)]

print(dp)