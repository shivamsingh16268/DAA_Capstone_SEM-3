
# Mini-Courier Planner

## Project Description
Mini-Courier Planner is a Python-based courier
planning application that uses Design and
Analysis of Algorithms to optimize parcel
selection and delivery routes.

## Algorithms Used

1. Merge Sort - Sorts parcels by priority.
2. 0/1 Knapsack - Selects parcels within vehicle capacity.
3. Dijkstra's Algorithm - Calculates shortest distances.
4. Nearest Neighbor TSP - Generates a delivery route.

## Technologies Used
- Python 3.11
- VS Code
- Matplotlib

## Project Structure

Mini-Courier-Planner/
- main.py
- sorting.py
- knapsack.py
- dijkstra.py
- tsp.py
- performance.py
- data/
- screenshots/
- README.md

## Installation

Install Matplotlib:

pip install matplotlib

## How to Run

Run the complete courier application:

python main.py

Run performance testing and generate graph:

python performance.py

## Sample Results

- Selected Parcels: 3
- Total Vehicle Weight: 10 kg
- Maximum Total Value: 130
- Delivery Route: A -> C -> B -> E -> A
- Total Route Distance: 20 km

## Time Complexity

- Merge Sort: O(n log n)
- 0/1 Knapsack: O(nW)
- Dijkstra: O((V+E) log V)
- Nearest Neighbor TSP: O(V^2) for greedy selection,
  excluding shortest-path preprocessing.

## Conclusion

The project demonstrates the application of
sorting, dynamic programming, graph algorithms
and approximation techniques in courier
planning.
