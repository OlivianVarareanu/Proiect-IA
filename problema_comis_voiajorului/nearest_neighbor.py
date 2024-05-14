import math

def calculate_distance(point1, point2):
    """
    Calculează distanța euclidiană între două puncte.
    """
    x1, y1 = point1
    x2, y2 = point2
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

def solve_tsp_nearest_neighbor(points):
    """
    Rezolvă problema comis-voiajorului folosind algoritmul cel mai apropiat vecin.
    """
    n = len(points)
    if n <= 1:
        return points

    # Alege un punct de start aleatoriu
    start_point = points[0]
    tour = [start_point]

    # Construiește turul
    while len(tour) < n:
        last_point = tour[-1]
        min_distance = float('inf')
        nearest_point = None

        # Găsește punctul cel mai apropiat
        for point in points:
            if point not in tour:
                distance = calculate_distance(last_point, point)
                if distance < min_distance:
                    min_distance = distance
                    nearest_point = point

        # Adaugă cel mai apropiat punct la tur
        tour.append(nearest_point)

    # Întoarce turul complet
    return tour

# Testare cu un set de puncte de exemplu
if __name__ == "__main__":
    # Definirea unui set de puncte de exemplu
    example_points = [(0, 0), (1, 2), (3, 4), (5, 6)]

    # Rezolvarea problemei comis-voiajorului folosind algoritmul cel mai apropiat vecin
    tour = solve_tsp_nearest_neighbor(example_points)

    # Afișarea turului rezultat
    print("Turul rezultat folosind algoritmul cel mai apropiat vecin:")
    print(tour)
