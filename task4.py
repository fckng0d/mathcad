print("Введите размер матрицы: ")
size = int(input())

def main(): 
    matrix = generate_square_spiral(size)
    print_matrix(matrix)
    diagonal_sum = 0
    diagonal_sum2 = 0   
    if (size % 2 == 0):    
        diagonal_sum = sum(matrix[i][i] for i in range(size+1))
        diagonal_sum2 = sum(matrix[i][size-i+1] for i in range(1, size+1))
    else:
        diagonal_sum = sum(matrix[i][i] for i in range(size))
        diagonal_sum2 = sum(matrix[i][size-i-1] for i in range(size))
    res = diagonal_sum + diagonal_sum2
    if (size % 2 != 0):
        res -= 1
    print("Сумма чисел на диагоналях:", res)

def generate_square_spiral(size):
    if size % 2 == 0:
        matrix = [[0] * (size + 1) for _ in range(size + 1)]
    else:
        matrix = [[0] * size for _ in range(size)]
    
    value = 1
    x, y = 0, 0
    dx, dy = 0, -1
    
    for _ in range(size * size):
        if -size // 2 <= x <= size // 2 and -size // 2 <= y <= size // 2:
            matrix[y + size // 2][x + size // 2] = value
            value += 1
        
        if x == y or (x < 0 and x == -y) or (x > 0 and x == 1 - y):
            dx, dy = -dy, dx
        
        x += dx
        y += dy
    
    return matrix

def print_matrix(matrix):
    size = len(matrix)
    for i in range(size):
        for j in range(size):
            print(f'{matrix[i][j]:>4}', end='')
        print()

if __name__ == '__main__':
    main()
