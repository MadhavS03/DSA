### Big O is comparing codes mathematically about how efficient they run ###
### Time complexity : A way to measure efficieny , measured in the number of operations that a code takes to complete ###
### Space complexity: How much memory a code takes up ###

### 3 letters while dealing with time and space complexity:
### Best case scenario - Omega
### Average case scenario - Theta
### Worst case scenario- Big O

### First Big O with code , with O(n)

def print_items(n):
    """print_items function accepts argument 'n' and will print a sequence of numbers from 0 to n-1"""
    for i in range (n):
        print(i)
      
print_items(10)

### O(n) is always proportional , a straight line in a graph 
