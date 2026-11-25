
# Mini-Courier Planner - Testing Documentation

## 1. Testing Overview

The Mini-Courier Planner was tested using sample
parcel data and a weighted delivery graph.

The testing verifies the correctness of all four
algorithms and measures their execution time.

## 2. Test Cases

### Test Case 1: Merge Sort
Input priorities: 2, 5, 1, 4, 3

Expected sorted priorities: 5, 4, 3, 2, 1

Result: Passed

### Test Case 2: 0/1 Knapsack
Vehicle capacity: 10 kg

Selected parcels: P1, P2, P4

Total weight: 10 kg

Maximum value: 130

Result: Passed

### Test Case 3: Dijkstra's Algorithm

Starting location: A

Shortest distances:
- A = 0 km
- B = 3 km
- C = 2 km
- D = 8 km
- E = 10 km

Result: Passed

### Test Case 4: Nearest Neighbor TSP

Starting location: A

Delivery route:
A -> C -> B -> D -> E -> A

Total distance: 20 km

Result: Passed

### Test Case 5: Complete Courier Planner

Selected parcels: 3

Total weight: 10 kg

Maximum value: 130

Final route:
A -> C -> B -> E -> A

Total distance: 20 km

Result: Passed

## 3. Performance Testing

Dataset sizes: 10, 20, 30, 40 and 50.

Each algorithm is executed five times and
average execution time is calculated.

## 4. Time Complexity

| Algorithm | Time Complexity |
|---|---|
| Merge Sort | O(n log n) |
| 0/1 Knapsack | O(nW) |
| Dijkstra | O((V+E) log V) |
| Nearest Neighbor TSP | O(V²) for route selection |

## 5. Conclusion

All four algorithms were implemented and tested.

The complete application successfully combines
parcel sorting, package selection, shortest-path
calculation and delivery route planning.
