import copy

def make_triangle(matrix):
    new_matrix = copy.deepcopy(matrix)
    rows = len(new_matrix)
    cols = len(new_matrix[0])

    print("\nПочаткова матриця:")
    for i in range(rows):
        print(new_matrix[i])

    print("\nОбмін рядків:")
    new_matrix.sort(key=lambda x: x[0], reverse=True)
    for i in range(rows):
        print(new_matrix[i])

    print("\nПриведення матриці до верхньотрикутного вигляду:")
    for i in range(min(rows, cols)):
        if new_matrix[i][i] != 0:
            scale_factor = 1.0 / new_matrix[i][i]
            for j in range(cols):
                new_matrix[i][j] *= scale_factor

        # Обнуління нижніх елементів у столбці
        for k in range(i + 1, rows):
            factor = new_matrix[k][i]
            for j in range(cols):
                new_matrix[k][j] -= factor * new_matrix[i][j]

    for row in new_matrix:
        print(row)
    return new_matrix

def gauss(new_matrix, matrix):
    rows = len(new_matrix)
    cols = len(new_matrix[0])
    solution = [0] * rows
    print("\nКорені:")
    for i in range(rows - 1, -1, -1):
        solution[i] = new_matrix[i][cols - 1]
        for j in range(i + 1, rows):
            solution[i] -= new_matrix[i][j] * solution[j]
            solution[i] /= new_matrix[i][i]
    i = 2
    while i > -1:
        print(f"x{i+1} = {solution[i]}")
        i -= 1

    print("\nПеревірка:")
    result = [[], [], []]
    for i in range(min(rows, cols)):
        for j in range(cols - 1):
            sol = matrix[i][j] * solution[j]
            result[i].append(sol)
    for sublist in result:
        subtotal = sum(sublist)
        sublist.append(subtotal)
    for sublist in result:
        print(f"{sublist[0]} + {sublist[1]} + {sublist[2]} = {sublist[3]}")

def main():
    print("Комп'ютерний практикум №2 \nВаріант №11 \nстудент групи ПБ-21 \nРозумняк Руслан")
    matrix = [
        [2.1, 2.8, 1.9, 0.2],
        [1.9, 3.1, 2.1, 2.1],
        [7.5, 3.8, 9.8, 5.6],
    ]
    print("\n___ Метод Гаусса ___")
    gauss(make_triangle(matrix), matrix)


if __name__ == '__main__':
    main()

