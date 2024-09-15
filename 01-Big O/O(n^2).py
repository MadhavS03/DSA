def print_items(n):
    for i in range (n):
        for j in range (n):
            print(i, j)
      
print_items(10)

### Printed from 00-99, 100 items
### n*n items printed, n^2
### O(n^2) on graph is much steeper than O(n), less efficient in time complexity point