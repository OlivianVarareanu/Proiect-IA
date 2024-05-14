import random
import math

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

def generate_neighbor(board):
    """
    Generează un vecin al tablei de șah printr-o mutație aleatoare.
    """
    n = len(board)
    neighbor = board.copy()
    random_index = random.randint(0, n - 1)
    random_value = random.randint(0, n - 1)
    neighbor[random_index] = random_value
    return neighbor

def simulated_annealing(n, initial_temperature=100, cooling_rate=0.95, max_iterations=1000):
    """
    Implementează algoritmul de simulare a anelării pentru problema celor N regine.
    """
    current_state = [random.randint(0, n - 1) for _ in range(n)]
    current_attacks = calculate_attacks(current_state)
    best_state = current_state
    best_attacks = current_attacks
    temperature = initial_temperature

    for _ in range(max_iterations):
        if current_attacks == 0:
            return current_state

        # Generăm un vecin
        neighbor = generate_neighbor(current_state)
        neighbor_attacks = calculate_attacks(neighbor)

        # Verificăm dacă vecinul este o soluție mai bună sau este acceptat pe baza temperaturii
        if neighbor_attacks < current_attacks or random.random() < math.exp((current_attacks - neighbor_attacks) / temperature):
            current_state = neighbor
            current_attacks = neighbor_attacks

        # Actualizăm cea mai bună soluție găsită până acum
        if current_attacks < best_attacks:
            best_state = current_state
            best_attacks = current_attacks

        # Scădem temperatura
        temperature *= cooling_rate

    return best_state

# Testare cu N = 8
if __name__ == "__main__":
    solution = simulated_annealing(8)
    if solution:
        print("Soluție găsită folosind algoritmul de simulare a anelării:")
        print(solution)
    else:
        print("Nu s-a găsit o soluție în numărul specificat de iterații.")
