my_list = [11, 3, 23, 7]

my_list.append(17)
print(my_list)

my_list.pop()
print(my_list)

### O(1)- Adding or removing from last of list 

my_list.pop(0)
print(my_list)

my_list.insert(0,11)
print(my_list)

### O(n)- adding or removing form start of list 

my_list.insert(1, 'hi')
print(my_list)

### O(n) - adding or removing from in between of list 
### O(n) - iterating through a list to find something based on VALUE
### O(1) - iterating to find something based on INDEX 