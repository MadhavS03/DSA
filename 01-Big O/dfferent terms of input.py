def print_items(a, b):
    for i in range(a):
        print(i)
    for j in range(b):
        print(j)
    
print_items(10,15)

### Big O of this code won't be O(n+n) or O(2n)
### for first for loop -> O(a)
### for second for loop -> O(b)
### so O(a+b)
### Similarly :

def print_items(a, b):
    for i in range (a):
        for j in range (b):
            print(i, j)
        
### O(a*b)