
from dijkstra import dijkstra


def nearest_neighbor_tsp(graph, start):
    # Calculate shortest distances between every pair
    all_distances = {}

    for node in graph:
        all_distances[node] = dijkstra(graph, node)

    unvisited = set(graph.keys())
    unvisited.remove(start)

    route = [start]
    current = start
    total_distance = 0

    # Visit the nearest unvisited location
    while unvisited:
        next_node = min(
            unvisited,
            key=lambda node: all_distances[current][node]
        )

        total_distance += all_distances[current][next_node]

        route.append(next_node)
        unvisited.remove(next_node)
        current = next_node

    # Return to the starting location
    total_distance += all_distances[current][start]
    route.append(start)

    return route, total_distance
