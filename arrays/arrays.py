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