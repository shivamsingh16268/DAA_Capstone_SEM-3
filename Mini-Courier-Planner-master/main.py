
import json

from sorting import merge_sort_parcels
from knapsack import knapsack
from dijkstra import dijkstra
from tsp import nearest_neighbor_tsp


# Load parcel data from JSON file
with open("data/parcels.json", "r") as file:
    dataset = json.load(file)

parcels = dataset["parcels"]
capacity = dataset["vehicle_capacity"]


# Road network (undirected weighted graph)
graph = {
    "A": {"B": 4, "C": 2},
    "B": {"A": 4, "C": 1, "D": 5},
    "C": {"A": 2, "B": 1, "D": 8, "E": 10},
    "D": {"B": 5, "C": 8, "E": 2},
    "E": {"C": 10, "D": 2}
}


def run_courier_planner():

    print("\n======================================")
    print("       MINI-COURIER PLANNER")
    print("======================================")

    # STEP 1: Display available parcels
    print("\n1. AVAILABLE PARCELS")

    for parcel in parcels:
        print(
            parcel["id"],
            "| Priority:", parcel["priority"],
            "| Deadline:", parcel["deadline"],
            "| Weight:", parcel["weight"], "kg",
            "| Value:", parcel["value"],
            "| Destination:", parcel["destination"]
        )

    # STEP 2: Sort parcels using Merge Sort
    print("\n2. PARCEL PRIORITIZATION (MERGE SORT)")

    sorted_parcels = merge_sort_parcels(parcels)

    for parcel in sorted_parcels:
        print(
            parcel["id"],
            "| Priority:", parcel["priority"],
            "| Deadline:", parcel["deadline"]
        )

    # STEP 3: Select parcels using 0/1 Knapsack
    print("\n3. OPTIMAL PACKAGE SELECTION (KNAPSACK)")

    max_value, selected_parcels = knapsack(
        sorted_parcels, capacity
    )

    total_weight = sum(
        parcel["weight"] for parcel in selected_parcels
    )

    print("Vehicle Capacity:", capacity, "kg")
    print("Selected Parcels:")

    for parcel in selected_parcels:
        print(
            parcel["id"],
            "| Weight:", parcel["weight"], "kg",
            "| Value:", parcel["value"],
            "| Destination:", parcel["destination"]
        )

    print("Total Weight:", total_weight, "kg")
    print("Maximum Total Value:", max_value)

    # STEP 4: Calculate shortest distances using Dijkstra
    print("\n4. SHORTEST DISTANCES (DIJKSTRA)")

    all_distances = {}

    for location in graph:
        all_distances[location] = dijkstra(graph, location)

    for location, distance in all_distances["A"].items():
        print("A to", location, ":", distance, "km")

    # STEP 5: Generate delivery route using TSP
    print("\n5. DELIVERY ROUTE (NEAREST NEIGHBOR TSP)")

    destinations = sorted({
        parcel["destination"]
        for parcel in selected_parcels
    })

    locations_to_visit = ["A"] + destinations

    # Create a complete graph using shortest distances
    route_graph = {}

    for location in locations_to_visit:
        route_graph[location] = {
            other: all_distances[location][other]
            for other in locations_to_visit
            if other != location
        }

    route, total_distance = nearest_neighbor_tsp(
        route_graph, "A"
    )

    print("Delivery Route:", " -> ".join(route))
    print("Total Route Distance:", total_distance, "km")

    # STEP 6: Display final courier plan
    print("\n======================================")
    print("          FINAL COURIER PLAN")
    print("======================================")

    print("Total Parcels Selected:", len(selected_parcels))
    print("Total Vehicle Weight:", total_weight, "kg")
    print("Vehicle Capacity:", capacity, "kg")
    print("Total Parcel Value:", max_value)
    print("Final Delivery Route:", " -> ".join(route))
    print("Total Delivery Distance:", total_distance, "km")

    print("\nCourier plan generated successfully!")


if __name__ == "__main__":
    run_courier_planner()
