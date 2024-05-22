#import matplotlib.pyplot as plt
from problema_regine import backtracking as queens_backtracking
from problema_regine import hill_climbing as queens_hill_climbing
from problema_regine import simulated_annealing as queens_simulated_annealing
from problema_regine import genetic_algorithm as queens_genetic_algorithm
#from problema_regine import plotting as queens_plotting
from problema_comis_voiajorului import backtracking as tsp_backtracking
from problema_comis_voiajorului import nearest_neighbor as tsp_nearest_neighbor
#from problema_comis_voiajorului import plotting as tsp_plotting

def display_info():
    print("Program realizat de Varareanu Vasile Olivian, Guliciuc Denis, Robert Timoficiuc, grupa 3133A")

example_points = [(0, 0), (1, 2), (3, 4), (5, 6)]

def main():
    while True:
        print("Selectați o opțiune:")
        print("a. Problema celor N regine (backtracking recursiv)")
        print("b. Problema celor N regine (alg. alpinistului)")
        print("c. Problema celor N regine (alg. calirii simulate)")
        print("d. Problema celor N regine (alg. genetic)")
        print("e. Plotare grafice problema celor N regine")
        print("f. Problema comis-voiajorului (backtracking recursiv)")
        print("g. Problema comis-voiajorului (alg. celui mai apropiat vecin)")
        print("h. Plotare grafice problema comis-voiajorului")
        print("x. Info")
        print("y. Exit")

        option = input("Opțiune: ")

        if option == 'a':
            n = int(input("Introduceți numărul de regine (N): "))
            solutions = queens_backtracking.solve_n_queens_backtracking(n)
            print("Numărul de soluții găsite:", len(solutions),"pentru dimensiunea ",n,)
            for solution in solutions:
                print(solution)
        elif option == 'b':
            n = int(input("Introduceți numărul de regine (N): "))
            solution = queens_hill_climbing.random_restart_hill_climbing(n)
            if solution:
                print("Soluție găsită folosind algoritmul Hill Climbing cu restartări aleatorii:")
                print(solution)
            else:
                print("Nu s-a găsit o soluție în numărul specificat de încercări.")

        elif option == 'c':
            n = int(input("Introduceți numărul de regine (N): "))
            solution = queens_simulated_annealing.simulated_annealing(n)
            if solution:
                print("Soluție găsită folosind algoritmul de simulare a anelării:")
                print(solution)
            else:
                print("Nu s-a găsit o soluție în numărul specificat de iterații.")
        elif option == 'd':
            n = int(input("Introduceți numărul de regine (N): "))
            solution, generations = queens_genetic_algorithm.solve_n_queens_genetic_algorithm(n)
            print("Soluție găsită folosind algoritmul genetic:")
            print(solution)
            print("Generații necesare:", generations)

        # elif option == 'e':
        #     queens_plotting.plot_queens_graph()  # Apelăm funcția din modulul de plotare a problemei celor N regine

        elif option == 'f':
            
            solution = tsp_nearest_neighbor.solve_tsp_nearest_neighbor(example_points)
            if solution:
                print("Soluție găsită folosind algoritmul de simulare a anelării:")
                print(solution)
            else:
                print("Nu s-a găsit o soluție în numărul specificat de iterații.")
        elif option == 'g':

            
            solution = tsp_nearest_neighbor.solve_tsp_nearest_neighbor(example_points)
            if solution:
                print("Soluție găsită folosind algoritmul de simulare a anelării:")
                print(solution)
            else:
                print("Nu s-a găsit o soluție în numărul specificat de iterații.")

        elif option == 'h':
            break
           # tsp_plotting.plot_tsp_graph()  # Apelăm funcția din modulul de plotare a problemei comis-voiajorului
        elif option == 'x':
            display_info()
        elif option == 'y':
            print("La revedere!")
            break  # Ieșiți din bucla while pentru a termina programul
        else:
            print("Opțiune invalidă.")

if __name__ == '__main__':
    main()
