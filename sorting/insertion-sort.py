
l1 = [9,2,62,4,3,5,21]

for i in range(1,len(l1)):
    key = l1[i]
    j = i - 1
    while j >=0 and l1[j] > key:
        l1[j+1] = l1[j]
        j = j - 1
 
    l1[j+1] = key

for i in l1:
    print(i)