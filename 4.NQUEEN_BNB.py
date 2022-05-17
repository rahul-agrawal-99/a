n= 20

def print_b(board):
    print(f"SOLUTION FOR {n}-QUEEN is")
    print("----"*n)
    for index,i in enumerate(board):
        for j in i:
            if j == 0:
                print(j, end='   ')
            else:
                print(f"Q{index+1}", end='  ')
        print()
    print("----"*n)


board = [ [0] * n for i in range(n) ]

diagonal = [False] * (2*n-1)        #row + col

rev_diagonal = [False] * (2*n-1)       #  row - col + n -1 

col_lookup = [False] * n


def issafe(row,col,d,rd ,col_lookup , b):
    if 1 not in b[row]:
        if not col_lookup[col]:
            if not d[row + col]:
                if not rd[row - col +n - 1]:
                    return True
    return False




def solution(b ,d ,rd , col_lookup , col ):    #  board , diagonal , rev_diagonal , collookup , col_num
    if (col >= n):
        return True
    for i in range(n):   # row
        if issafe(i , col , d , rd , col_lookup , b):   # row , col , diagonal , rev_diagonal , collookup
            b[i][col] = 1
            d[i+col] = True
            rd[i-col+n-1] = True
            col_lookup[col] = True
                
            if solution(b , d , rd , col_lookup , col + 1):
                return True
            
            b[i][col] = 0
            d[i+col] = False
            rd[i-col+n-1] = False
            col_lookup[col] = False
    
    return False
    
 
if solution(board,diagonal,rev_diagonal,col_lookup , 0) != False:  
    print_b(board)
else:
    print("No SOLUTION")
            
            
   
  