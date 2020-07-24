


from heapq import heappush as push, heappop as pop , heapify as make 
import sys
import resource

sys.setrecursionlimit(10 ** 6)
resource.setrlimit(resource.RLIMIT_STACK, (2 ** 29, 2 ** 30))
tree = {}
def expand(x, y):
    global tree
    a = x[1]
    b = y[1]
    for node in a.split():
        try:
            tree[node] += "0"
        except KeyError:
            tree[node] = "0"
    for node in b.split():
        try:
            tree[node] += "1"
        except KeyError:
            tree[node] = "1"
    
            
def huffman(freq):
    global tree
    if len(freq) == 2 :
        expand(freq[0] , freq[1])
    else:
        a = pop(freq)
        b = pop(freq)
        push(freq , (a[0]+b[0] , a[1]+" "+b[1]) )    
        huffman(freq)
        expand(a , b)
        

freq = []
with open('alg_data.txt') as f:
    n = int(f.readline())
    data = f.readlines()
    i = 1
    for line in data:
        freq.append( (int(line[:-1]) , str(i)) )
        i += 1
       
make(freq)
huffman(freq)
binary_code = sorted(list(tree.values()), key = lambda x : len(x))
print(len(binary_code[n-1]) , len(binary_code[0]))

