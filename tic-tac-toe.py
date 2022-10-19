from typing import Set, List


def make_move(matrix: List[List[str]], symbol: str):
    print("Участник " + symbol + " , введите номер строки и столбца")
    y = int(input("row ")) - 1
    x = int(input("col ")) - 1
    matrix[y][x] = symbol


def is_finished(matrix: List[List[str]]) -> bool:
    N = len(matrix)

    def check(cells: Set[str]) -> bool:
        return cells == set("X") or cells == set("O")

    def check_rows() -> bool:
        for y in range(N):
            if check(set(matrix[y])):
                return True

        return False

    def check_cols() -> bool:
        for x in range(N):
            if check(set(matrix[y][x] for y in range(N))):
                return True

        return False

    def check_diags():
        d1 = set(matrix[i][i] for i in range(N))
        d2 = set(matrix[N - i - 1][i] for i in range(N))
        return check(d1) or check(d2)

    return check_rows() or check_cols() or check_diags()


def print_matrix(matrix: List[List[str]]):
    for row in matrix:
        print(' '.join([str(elem) for elem in row]))


def main():
    N = 3
    matrix = [["-"] * N for i in range(N)]

    symbol = "X"
    while True:
        make_move(matrix, symbol)
        print_matrix(matrix)
        if is_finished(matrix):
            print("Done!")
            break

        symbol = "O" if symbol == "X" else "X"


main()
