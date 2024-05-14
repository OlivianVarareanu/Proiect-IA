import random

def calculate_attacks(board):
    """
    Calculează numărul de atacuri între regine pe tabla de șah.
    """
    n = len(board)
    attacks = 0
    for i in range(n):
        for j in range(i + 1, n):
            if board[i] == board[j] or \
               board[i] - i == board[j] - j or \
               board[i] + i == board[j] + j:
                attacks += 1
    return attacks

def random_restart_hill_climbing(n, max_attempts=10000):
    """
    Implementează algoritmul Hill Climbing cu restartări aleatorii.
    """
    current_state = [random.randint(0, n-1) for _ in range(n)]
    current_attacks = calculate_attacks(current_state)
    attempts = 0

    while attempts < max_attempts:
        if current_attacks == 0:
            return current_state

        # Generează o vecinătate a stării curente
        neighbor = current_state.copy()
        random_index = random.randint(0, n-1)
        random_value = random.randint(0, n-1)
        neighbor[random_index] = random_value

        # Calculează numărul de atacuri al vecinului
        neighbor_attacks = calculate_attacks(neighbor)

        # Actualizează starea curentă dacă vecinul are mai puține atacuri
        if neighbor_attacks < current_attacks:
            current_state = neighbor
            current_attacks = neighbor_attacks
        else:
            # Dacă nu se poate îmbunătăți, restartează căutarea
            current_state = [random.randint(0, n-1) for _ in range(n)]
            current_attacks = calculate_attacks(current_state)
            attempts += 1

    # În cazul în care nu se găsește o soluție în numărul de încercări specificat
    return None

# Testare cu N = 8
if __name__ == "__main__":
    solution = random_restart_hill_climbing(5)
    if solution:
        print("Soluție găsită folosind algoritmul Hill Climbing cu 5 restartări aleatorii:")
        print(solution)
    else:
        print("Nu s-a găsit o soluție în numărul specificat de încercări.")
