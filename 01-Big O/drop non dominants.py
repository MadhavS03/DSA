### Another simplification technique for Big O

def print_items(n):
    for i in range (n):
        for j in range (n):
            print(i, j)
    for k in range(n):
        print(k)

print_items(10)

### Nested for loops printed 00-99 -> O(n^2)
### Single for loop printed 0-9 -> O(n)
### Total = O(n^2 + n)
### What if n is a ver large number than , n^2 would aways be the more dominant one and n less dominant 
### Drop the n , Drop the non dominants