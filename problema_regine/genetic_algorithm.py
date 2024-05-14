import random

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

def generate_random_chromosome(n):
    """
    Generează un cromozom aleatoriu, reprezentând o soluție pentru problema celor N regine.
    """
    return [random.randint(0, n-1) for _ in range(n)]

def crossover(chromosome1, chromosome2):
    """
    Realizează operația de crossover între doi cromozomi.
    """
    n = len(chromosome1)
    crossover_point = random.randint(1, n - 1)
    child1 = chromosome1[:crossover_point] + chromosome2[crossover_point:]
    child2 = chromosome2[:crossover_point] + chromosome1[crossover_point:]
    return child1, child2

def mutate(chromosome, mutation_rate):
    """
    Realizează operația de mutație asupra unui cromozom cu o anumită rată de mutație.
    """
    n = len(chromosome)
    mutated_chromosome = chromosome[:]
    for i in range(n):
        if random.random() < mutation_rate:
            mutated_chromosome[i] = random.randint(0, n - 1)
    return mutated_chromosome

def calculate_fitness(chromosome):
    """
    Calculează valoarea de fitness a unui cromozom, reprezentând câte perechi de regine nu se atacă.
    """
    n = len(chromosome)
    attacks = 0
    for i in range(n):
        for j in range(i + 1, n):
            if chromosome[i] == chromosome[j] or \
               chromosome[i] - i == chromosome[j] - j or \
               chromosome[i] + i == chromosome[j] + j:
                attacks += 1
    return n * (n - 1) / 2 - attacks

def select_parent(population):
    """
    Selectează un părinte din populația dată bazat pe valoarea de fitness.
    """
    total_fitness = sum(calculate_fitness(chromosome) for chromosome in population)
    selection_point = random.uniform(0, total_fitness)
    current_fitness = 0
    for chromosome in population:
        current_fitness += calculate_fitness(chromosome)
        if current_fitness > selection_point:
            return chromosome

def solve_n_queens_genetic_algorithm(n, population_size=100, mutation_rate=0.01, max_generations=1000):
    """
    Rezolvă problema celor N regine folosind algoritmul genetic.
    """
    population = [generate_random_chromosome(n) for _ in range(population_size)]
    generations = 0

    while generations < max_generations:
        # Selectează părinții
        parent1 = select_parent(population)
        parent2 = select_parent(population)

        # Realizează crossover
        child1, child2 = crossover(parent1, parent2)

        # Realizează mutație
        child1 = mutate(child1, mutation_rate)
        child2 = mutate(child2, mutation_rate)

        # Înlocuiește părinții cu copiii în populație
        population.extend([child1, child2])

        # Seleționează cei mai buni cromozomi pentru următoarea generație
        population = sorted(population, key=lambda x: calculate_fitness(x), reverse=True)[:population_size]

        # Verifică dacă am găsit o soluție perfectă
        best_chromosome = max(population, key=lambda x: calculate_fitness(x))
        if calculate_fitness(best_chromosome) == n * (n - 1) / 2:
            return best_chromosome, generations

        generations += 1

    # Returnează cel mai bun cromozom găsit și numărul de generații necesare
    return max(population, key=lambda x: calculate_fitness(x)), generations


# Testare cu N = 8
if __name__ == "__main__":
    solution, generations = solve_n_queens_genetic_algorithm(8)
    print("Soluție găsită folosind algoritmul genetic:")
    print(solution)
    print("Generații necesare:", generations)
