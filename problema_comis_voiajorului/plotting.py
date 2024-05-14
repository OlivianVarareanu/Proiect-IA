import matplotlib.pyplot as plt

def plot_tsp_graph(points, tour=None):
    """
    Plotează graficul asociat problemei comis-voiajorului.

    Args:
        points (list): Lista de puncte (coordonate) în plan.
        tour (list, optional): Turul (ordinul) în care sunt vizitate punctele. 
            Default este None, ceea ce înseamnă că turul nu este plotat.
    """
    x_values = [point[0] for point in points]
    y_values = [point[1] for point in points]

    plt.figure(figsize=(8, 6))
    plt.scatter(x_values, y_values, color='blue', label='Puncte')

    if tour:
        # Adaugă linii între punctele din tur pentru a arăta ordinea de vizitare
        for i in range(len(tour) - 1):
            point1 = points[tour[i]]
            point2 = points[tour[i + 1]]
            plt.plot([point1[0], point2[0]], [point1[1], point2[1]], color='red')

        # Adaugă o linie între ultimul punct și primul punct pentru a închide ciclul
        point1 = points[tour[-1]]
        point2 = points[tour[0]]
        plt.plot([point1[0], point2[0]], [point1[1], point2[1]], color='red')

    plt.title('Graficul problemei comis-voiajorului')
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.legend()
    plt.grid(True)
    plt.show()

# Testare cu un set de puncte de exemplu
if __name__ == "__main__":
    # Definirea unui set de puncte de exemplu
    example_points = [(0, 0), (1, 2), (3, 4), (5, 6)]

    # Plotarea graficului asociat cu problema comis-voiajorului (fără tur)
    plot_tsp_graph(example_points)

    # Plotarea graficului asociat cu problema comis-voiajorului (cu tur)
    example_tour = [0, 1, 2, 3]  # Turul de exemplu
    plot_tsp_graph(example_points, tour=example_tour)
