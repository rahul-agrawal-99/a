n= 4

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




def issafe(row,col,b):
    if 1 not in b[row]:
        for i in range(col):
            if b[row][i] == 1:
                return False
        
        r , c = row , col
        while(r < n and c < n):
            if b[r][c] == 1:
                return False
            r = r + 1
            c = c + 1
            
        r , c = row , col
        while(r >= 0  and c >= 0):
            if b[r][c] == 1:
                return False
            r = r - 1
            c = c - 1
        r , c = row , col
        
        while(r < n   and c >= 0):
            if b[r][c] == 1:
                return False
            r = r + 1
            c = c - 1
            
        r , c = row , col
        while(r >= 0  and c < n):
            if b[r][c] == 1:
                return False
            r = r - 1
            c = c + 1
        return True
    
    return False




def solution(b  , col ):    #  board  , col_num
    if (col >= n):
        return True
    for i in range(n):   # row
        if issafe(i , col  , b):   # row , col , diagonal , rev_diagonal , collookup
            b[i][col] = 1
      
                
            if solution(b ,  col + 1):
                return True
            
            b[i][col] = 0
  
    return False
    
 
if solution(board,  0) != False:  
    print_b(board)
else:
    print("No SOLUTION")
            
            
   
  