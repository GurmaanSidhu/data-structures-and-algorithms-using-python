fruits = ['apple', 'mango', 'banana', 'papaya', 'kiwi', 'apple']

# Count - checks for how many times the elements are being repeated.
print(fruits.count("apple")) 

# Index - finds that particular elements index
print(fruits.index("banana"))
print(fruits.index("apple", 3)) # finds the index of apple after the 3 index- i.e. 5

#Appends
fruits.append("kiwi")
print(fruits)

# Extend - unlike append - it adds another list at the back of it
vegitables = ['tomato', 'bringle', 'coliflower']
vegitables.extend(fruits)
print(vegitables)

# Inserts an element at a particular index
fruits.insert(2, 'guava')
print(fruits)

fruits.remove("guava")
print(fruits)

fruits.pop(1)
print(fruits)

vegitables.clear()
print(vegitables)

fruits.reverse()


# STACKS
# stack = [3, 4, 5]
# stack.append(6)
# stack.append(7)
# stack
# [3, 4, 5, 6, 7]
# stack.pop()
# 7
# stack
# [3, 4, 5, 6]
# stack.pop()
# 6
# stack.pop()
# 5
# stack
# [3, 4]

# QUEUES
# from collections import deque
# queue = deque(["Eric", "John", "Michael"])
# queue.append("Terry")           # Terry arrives
# queue.append("Graham")          # Graham arrives
# queue.popleft()                 # The first to arrive now leaves
# 'Eric'
# queue.popleft()                 # The second to arrive now leaves
# 'John'
# queue                           # Remaining queue in order of arrival
# deque(['Michael', 'Terry', 'Graham'])


# List Comprehensions
# squares = []
# for x in range(10):
#     squares.append(x**2)
# squares - >[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

# squares = list(map(lambda x: x**2, range(10)))
# squares = [x**2 for x in range(10)]
# [(x, y) for x in [1,2,3] for y in [3,1,4] if x != y]
# [(1, 3), (1, 4), (2, 3), (2, 1), (2, 4), (3, 1), (3, 4)]
# combs = []
# for x in [1,2,3]:
#     for y in [3,1,4]:
#         if x != y:
#             combs.append((x, y))

# combs ->[(1, 3), (1, 4), (2, 3), (2, 1), (2, 4), (3, 1), (3, 4)]

# vec = [-4, -2, 0, 2, 4]
# # create a new list with the values doubled
# [x*2 for x in vec]
# [-8, -4, 0, 4, 8]
# # filter the list to exclude negative numbers
# [x for x in vec if x >= 0]
# [0, 2, 4]
# # apply a function to all the elements
# [abs(x) for x in vec]
# [4, 2, 0, 2, 4]
# # call a method on each element
# freshfruit = ['  banana', '  loganberry ', 'passion fruit  ']
# [weapon.strip() for weapon in freshfruit]
# ['banana', 'loganberry', 'passion fruit']
# # create a list of 2-tuples like (number, square)
# [(x, x**2) for x in range(6)]
# [(0, 0), (1, 1), (2, 4), (3, 9), (4, 16), (5, 25)]
# # the tuple must be parenthesized, otherwise an error is raised
# [x, x**2 for x in range(6)]
#   File "<stdin>", line 1
#     [x, x**2 for x in range(6)]
#      ^^^^^^^
# SyntaxError: did you forget parentheses around the comprehension target?
# # flatten a list using a listcomp with two 'for'
# vec = [[1,2,3], [4,5,6], [7,8,9]]
# [num for elem in vec for num in elem]
# [1, 2, 3, 4, 5, 6, 7, 8, 9]


# from math import pi
# [str(round(pi, i)) for i in range(1, 6)]
# ['3.1', '3.14', '3.142', '3.1416', '3.14159']


# Nested List Comprehensions
# matrix = [
#     [1, 2, 3, 4],
#     [5, 6, 7, 8],
#     [9, 10, 11, 12],
# ]

# transpose
# [[row[i] for row in matrix] for i in range(4)]
# [[1, 5, 9], [2, 6, 10], [3, 7, 11], [4, 8, 12]]

# transposed = []
# for i in range(4):
#     transposed.append([row[i] for row in matrix])

# transposed
# [[1, 5, 9], [2, 6, 10], [3, 7, 11], [4, 8, 12]]

# transposed = []
# for i in range(4):
#     # the following 3 lines implement the nested listcomp
#     transposed_row = []
#     for row in matrix:
#         transposed_row.append(row[i])
#     transposed.append(transposed_row)

# transposed
# [[1, 5, 9], [2, 6, 10], [3, 7, 11], [4, 8, 12]]

# print(list(zip(*matrix)))
# [(1, 5, 9), (2, 6, 10), (3, 7, 11), (4, 8, 12)]

# The del statement
# a = [-1, 1, 66.25, 333, 333, 1234.5]
# del a[0]
# a
# [1, 66.25, 333, 333, 1234.5]
# del a[2:4]
# a
# [1, 66.25, 1234.5]
# del a[:]
# a
# []

