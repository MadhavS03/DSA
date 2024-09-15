### Drop Constants ###
### A way to simplify the Big O ###

def print_items(n):
    for i in range (n):
        print(i)
    for j in range (n):
        print(j)  
      
print_items(10)

### Printed 0-9 2 times , total 20 times 
### (n+n) = (2n) , O(2n)
### Dropping the constant: O(n), doesn't matter even if it is O(100n) 