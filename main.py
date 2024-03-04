import copy
import numpy as np

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
    test(rows, cols, solution, matrix)

def test(rows, cols, solution, matrix):
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

    measurement_error(matrix, result)

def gordan(matrix):
    new_matrix = make_triangle(matrix)
    rows = len(new_matrix)
    cols = len(new_matrix[0])
    print("\nПриведення матриці до діагонального вигляду:")
    for i in range(min(rows, cols)):
        for k in range(rows):
            if k != i:
                factor = new_matrix[k][i]
                for j in range(cols):
                    new_matrix[k][j] -= factor * new_matrix[i][j]
    for row in new_matrix:
        print(row)

    print("\nКорені:")
    solution = []
    for i in range(0,3):
        solution.append(new_matrix[i][3])
        print(f"x{i + 1} = {solution[i]}")
    test(rows, cols, solution, matrix)
    return new_matrix

def measurement_error(matrix, roots):
    matrix_roots = []
    my_roots = []
    print("\nПохибка:")
    for i in range(0,3):
        matrix_roots.append(matrix[i][3])
        my_roots.append(roots[i][3])
        print(f"Δx{i+1} = |{matrix_roots[i]} - {my_roots[i]}| = {abs(my_roots[i] - matrix_roots[i])}")

def optimal(matrix):
    new_matrix = copy.deepcopy(matrix)
    rows = len(new_matrix)
    cols = len(new_matrix[0])

    max_value = 0
    index = -1
    # 1 строка
    for i in range(min(rows, cols)):
        if max_value < abs(new_matrix[0][i]):
            max_value = new_matrix[0][i]
            index = i
    print(f"\nМаксимальне значення у першому рядку за модулем = {max_value}")
    for i in range(cols):
        new_matrix[0][i] = new_matrix[0][i]/max_value
    copy_matrix = copy.deepcopy(new_matrix)
    print_matrix(copy_matrix)
    # 2 строка____________________________________________

    for i in range(cols):
        copy_matrix[1][i] -= new_matrix[0][i] * new_matrix[1][1]
    new_matrix = copy.deepcopy(copy_matrix)
    max_value = 0
    for i in range(min(rows, cols)):
        if max_value < abs(copy_matrix[1][i]):
            max_value = abs(copy_matrix[1][i])
    print(f"\nМаксимальне значення у другому рядку за модулем = {max_value}")
    print_matrix(copy_matrix)
    for i in range(cols):
        copy_matrix[1][i] /= -max_value

    # 3 строка__________________________
    for i in range(cols):
        copy_matrix[2][i] -= new_matrix[0][i] * new_matrix[2][1]
    new_matrix = copy.deepcopy(copy_matrix)
    max_value = 0
    for i in range(min(rows, cols)):
        if max_value < abs(copy_matrix[2][i]):
            max_value = abs(copy_matrix[2][i])
            index = i
    print(f"\nМаксимальне значення у третьому рядку за модулем = {max_value}")
    print_matrix(copy_matrix)
    for i in range(cols):
        copy_matrix[0][i] -= new_matrix[1][i] * new_matrix[0][0]
        copy_matrix[2][i] -= new_matrix[1][i] * new_matrix[2][0]
    new_matrix = copy.deepcopy(copy_matrix)
    for i in range(cols):
        copy_matrix[2][i] = new_matrix[2][i]/max_value
    new_matrix = copy.deepcopy(copy_matrix)
    for i in range(cols):
        copy_matrix[0][i] -= new_matrix[2][i] * new_matrix[0][2]

    print_matrix(copy_matrix)

    print("\nКорені:")
    solution = []
    solution.append(copy_matrix[1][3])
    solution.append(copy_matrix[0][3])
    solution.append(copy_matrix[2][3])
    for i in range(0, 3):
        print(f"x{i + 1} = {solution[i]}")
    test(rows, cols, solution, matrix)
    return copy_matrix

def simple_iterations(matrix):
    new_matrix = copy.deepcopy(matrix)
    rows = len(new_matrix)
    cols = len(new_matrix[0])
    print("\nПочаткова матриця")
    print_matrix(new_matrix)
    for i in range(rows):
        diag_elem = abs(new_matrix[i][i])
        sum_except_diag = sum(abs(x) for j, x in enumerate(new_matrix[i]) if j != i) - abs(new_matrix[i][3])
        if round(diag_elem, 1) == round(sum_except_diag, 1):
            print(f"{round(diag_elem, 3)} ={round(sum_except_diag, 3)} - умова не виконується")
        elif round(diag_elem, 1) > round(sum_except_diag, 1):
            print(f"{round(diag_elem, 3)} > {round(sum_except_diag, 3)} - умова виконується")
        elif round(diag_elem, 1) < round(sum_except_diag, 1):
            print(f"{round(diag_elem, 3)} < {round(sum_except_diag, 3)} - умова не виконується")
        print("Приведемо систему рівнянь до виду, що забезпечує збіжність методу простих ітерацій.\n")
    for i in range(rows - 2):
        print("Приведення до верхньотрикутного вигляду:")
        print_matrix(new_matrix)
        for i in range(len(matrix[0])):
            new_matrix[0][i] = (new_matrix[0][i] / 2.1)
        print_matrix(new_matrix)
        for i in range(len(matrix[0])):
            new_matrix[1][i] = new_matrix[1][i] - new_matrix[0][i] * 1.9
            new_matrix[2][i] = new_matrix[2][i] - new_matrix[0][i] * 7.5
        print_matrix(new_matrix)
        for i in range(len(matrix[0])):
            new_matrix[0][i] = (new_matrix[0][i] * 5)
            new_matrix[2][i] = new_matrix[2][i] + new_matrix[1][i] * 5
        print_matrix(new_matrix)
        for i in range(len(matrix[0])):
            new_matrix[0][i] = new_matrix[0][i] - new_matrix[1][i] * 8
        print_matrix(new_matrix)
        for i in range(rows):
            diagonal_element = abs(new_matrix[i][i])
            sum_except_diagonal = sum(abs(x) for j, x in enumerate(new_matrix[i])
                                  if j != i) - abs(new_matrix[i][3])
            print(f"{round(diagonal_element, 3)} > {round(sum_except_diagonal, 3)}")
    print("")
    x1 = 0
    x2 = 0
    x3 = 0
    for i in range(10):
        x1 = (-1 * new_matrix[0][1] * x2 + (- 1 * new_matrix[0][2]) * x3 - 14.885) / 5
        x2 = (-1 * new_matrix[1][2] * x3 + 1.92) / 0.567
        x3 = ((-1 * new_matrix[2][1] * x2) + 14.49) / 4.918
        print(f"Ітерація №{i + 1}; i = {i}")
        print(f"x1^{i} = {x1}\nx2^{i} = {x2}\nx3^{i} = {x3}\n")
    print(f"Корені:")
    solution = [x1,x2,x3]
    for i in range(0, 3):
        solution.append(new_matrix[i][3])
        print(f"x{i + 1} = {solution[i]}")
    test(rows, cols, solution, matrix)


def print_matrix(matrix):
    print("\n")
    for row in matrix:
        print(row)

def main():
    print("Комп'ютерний практикум №2 \nВаріант №11 \nстудент групи ПБ-21 \nРозумняк Руслан")

    matrix = [
        [2.1, 2.8, 1.9, 0.2],
        [1.9, 3.1, 2.1, 2.1],
        [7.5, 3.8, 9.8, 5.6],
    ]

    print("\n___ Метод Гаусса ___")
    gauss(make_triangle(matrix), matrix)
    print("\n___ Метод Жордана-Гаусса ___")
    gordan(matrix)
    print("\n___Метод оптимального виключення___")
    optimal(matrix)
    print("\n___Метод простих ітерацій___")
    simple_iterations(matrix)


if __name__ == '__main__':
    main()

