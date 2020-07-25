def knapsack(items,num,size):
    cache = [[],[]]
    for k in range(0,size+1):
        cache[0].append(0)
        cache[1].append(0)
    for i in range(1,num+1):
        for k in range(1,size+1):
            if k < items[i][1]:
                cache[1][k] = cache[0][k]
            else:
                cache[1][k] = max(cache[0][k] , cache[0][k-items[i][1]] + items[i][0])
        cache[0],cache[1] = cache[1],cache[0]
    return cache[0][size] 


items = [(0,0)]
with open('alg_data.txt') as f:
    first_line = f.readline()[:-1]
    first_line = first_line.split()
    size, number_of_items = first_line
    data = f.readlines()
    for line in data:
        elements = list(map(int,line[:-1].split()))
        items.append((elements[0],elements[1]))
f.close()
print(knapsack(items,int(number_of_items),int(size)))
