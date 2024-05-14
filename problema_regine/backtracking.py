def is_safe(board, row, col):
    """
    Verifică dacă este în siguranță să plasezi o regină în poziția (row, col) pe tablă.
    """
    # Verificăm coloanele anterioare din aceeași linie
    for i in range(col):
        if board[i] == row or \
           board[i] - i == row - col or \
           board[i] + i == row + col:
            return False
    return True

def solve_n_queens_backtracking_util(board, col, solutions):
    """
    Funcție utilitară pentru a rezolva problema celor N regine folosind backtracking.
    """
    n = len(board)
    if col >= n:
        solutions.append(list(board))
        return

    for row in range(n):
        if is_safe(board, row, col):
            board[col] = row
            solve_n_queens_backtracking_util(board, col + 1, solutions)
            board[col] = -1  # Resetăm poziția reginei pentru a încerca alte opțiuni

def solve_n_queens_backtracking(n):
    """
    Funcția principală pentru a rezolva problema celor N regine folosind backtracking.
    """
    board = [-1] * n  # Inițializăm tabla de șah cu -1 (nu sunt regine plasate)
    solutions = []  # Listă pentru a stoca soluțiile

    solve_n_queens_backtracking_util(board, 0, solutions)

    return solutions

# Testare cu N = 4
if __name__ == "__main__":
    solutions = solve_n_queens_backtracking(4)
    if solutions:
        print("Numărul de soluții găsite:", len(solutions))
        for solution in solutions:
            print(solution)
    else:
        print("Nu există soluții pentru problema celor 4 regine.")
