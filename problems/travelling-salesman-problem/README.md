# Travelling Salesman Problem

Given a list of city coordinates (eg. (23.33, 455.0), (23,4), (0.05, 0.09) ), calculate the shortest path that visits all cities only **once**, and returns to the first city. The algorithm should return/print the total path length.

## WARNING: The complexity for the problem can be O(2!) so running the algorithm on N > 15 is not advised. O(n^2 * 2^n) algorithms can handle around N = 20

```python
cites = { 1: City(0.14, 100), 2 : City(234.3, 21.1), ... }
tsp(cities) # > 776.0021
```
