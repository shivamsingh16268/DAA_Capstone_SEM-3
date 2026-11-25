
import time
import random
import os
import matplotlib.pyplot as plt

from sorting import merge_sort_parcels
from knapsack import knapsack
from dijkstra import dijkstra
from tsp import nearest_neighbor_tsp


def generate_graph(size):
    graph = {f"L{i}": {} for i in range(size)}

    for i in range(size):
        for j in range(i + 1, size):
            weight = random.randint(1, 20)
            graph[f"L{i}"][f"L{j}"] = weight
            graph[f"L{j}"][f"L{i}"] = weight

    return graph


def measure_time(function, repetitions=5):
    total_time = 0

    for _ in range(repetitions):
        start = time.perf_counter()
        function()
        end = time.perf_counter()
        total_time += (end - start) * 1000

    return total_time / repetitions


def run_performance_tests():
    random.seed(42)

    sizes = [10, 20, 30, 40, 50]

    sorting_times = []
    knapsack_times = []
    dijkstra_times = []
    tsp_times = []

    print("\n===== COURIER PLANNER PERFORMANCE TESTING =====")
    print("Average execution time (5 runs), in milliseconds\n")
    print("Size | Sorting | Knapsack | Dijkstra | TSP")
    print("-" * 60)

    for size in sizes:

        parcels = [
            {
                "id": f"P{i}",
                "priority": random.randint(1, 10),
                "deadline": random.randint(1, 30),
                "weight": random.randint(1, 20),
                "value": random.randint(10, 100)
            }
            for i in range(size)
        ]

        graph = generate_graph(size)

        sorting_time = measure_time(
            lambda: merge_sort_parcels(parcels)
        )

        knapsack_time = measure_time(
            lambda: knapsack(parcels, 100)
        )

        dijkstra_time = measure_time(
            lambda: dijkstra(graph, "L0")
        )

        tsp_time = measure_time(
            lambda: nearest_neighbor_tsp(graph, "L0")
        )

        sorting_times.append(sorting_time)
        knapsack_times.append(knapsack_time)
        dijkstra_times.append(dijkstra_time)
        tsp_times.append(tsp_time)

        print(
            f"{size:4} | {sorting_time:8.4f} | "
            f"{knapsack_time:8.4f} | "
            f"{dijkstra_time:8.4f} | "
            f"{tsp_time:8.4f}"
        )

    # Create runtime comparison graph
    plt.figure(figsize=(10, 6))

    plt.plot(sizes, sorting_times, marker="o", label="Merge Sort")
    plt.plot(sizes, knapsack_times, marker="o", label="Knapsack")
    plt.plot(sizes, dijkstra_times, marker="o", label="Dijkstra")
    plt.plot(sizes, tsp_times, marker="o", label="Nearest Neighbor TSP")

    plt.xlabel("Dataset Size (Number of Parcels / Locations)")
    plt.ylabel("Average Execution Time (milliseconds)")
    plt.title("Performance Comparison of Courier Planning Algorithms")

    plt.legend()
    plt.grid(True)
    plt.tight_layout()

    os.makedirs("screenshots", exist_ok=True)

    plt.savefig(
        "screenshots/runtime_comparison.png",
        dpi=300
    )

    print("\nRuntime graph saved successfully!")
    print("Location: screenshots/runtime_comparison.png")

    plt.show()


if __name__ == "__main__":
    run_performance_tests()
    