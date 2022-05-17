n = 3
opend = []      # for childs that to be processed
closed = []     # removed childs due to high f(n) value
path = []       # stores path that is being follwed

start_state =  [ ['2', '8', '3'],
                 ['1', '6', '4'], 
                 ['7', '_', '5']]


goal =  [['1', '2', '3'], 
         ['8', '_', '4'], 
         ['7', '6', '5']]


def f(start,goal):     #  number of misplaced tiles + level of node
        return h(start.data,goal)+start.level

def h(start,goal):
    temp = 0
    for i in range(0,3):
        for j in range(0,3):
            if start[i][j] != goal[i][j] and start[i][j] != '_':
                temp += 1
    return temp

def get_pos(puz,x):
    for i in range(0,3):
        for j in range(0,3):
            if puz[i][j] == x:
                return i,j
def copy(root):
    temp = []
    for i in root:
        t = []
        for j in i:
            t.append(j)
        temp.append(t)
    return temp 


def print_b(root):
    for i in range(n):  
        for j in range(n):  
            print(root[i][j],end=' ')
        print()


class Node:
    def __init__(self,data,level,fval):
        self.data = data
        self.level = level
        self.fval = fval


    def generate_child(self):
  
        x,y = get_pos(self.data,'_')

        val_list = [[x,y-1],[x,y+1],[x-1,y],[x+1,y]]
        children = []
        for i in val_list:
            x2 , y2 = i[0], i[1]
            if x2 >= 0 and x2 < n and y2 >= 0 and y2 < n:
                temp_puz = copy(self.data)
                temp = temp_puz[x2][y2]
                temp_puz[x2][y2] = temp_puz[x][y]
                temp_puz[x][y] = temp
                child_node = Node(temp_puz,self.level+1,0)
                children.append(child_node)
        
                
        return children
     
    




start = Node(start_state,0,0)
      
start.fval = f(start,goal)
opend.append(start)
while True:
    cur = opend[0]
    path.append([cur.data , cur.fval])
    if(h(cur.data,goal) == 0):  # Goal
        break
    for i in cur.generate_child():
        i.fval = f(i,goal)
        opend.append(i)
    closed.append(cur)
    del opend[0]
    opend.sort(key = lambda x:x.fval,reverse=False)



print("Reached Goal State with Heuristic Value Of : ",len(path)-1)

print("\n\n")
for i in path:
    print_b(i[0])
    print("F value is : ",i[1])
    print("------------    ")



