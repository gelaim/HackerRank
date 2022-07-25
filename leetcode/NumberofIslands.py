class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        nIslands = 0
        
        
        visited = set()
        def bfs(row, column):
            queue = collections.deque()
            queue.append((row,column))
            
            while len(queue) > 0:
                curr_row, curr_col = queue.popleft()
                directions = [[1,0], [0,1],[-1,0],[0,-1]]
                
                for dir_r,dir_c in directions:
                    row = curr_row + dir_r
                    col = curr_col + dir_c
                    
                    if (row >=0 and row <len(grid) and
                        col >=0 and col < len(grid[0]) and
                        grid [row] [col] =="1" and (row,col) not in visited):
                        queue.append((row,col))
                        visited.add((row,col))        
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == "1" and (r,c) not in visited:
                    visited.add((r,c))
                    nIslands += 1
                    bfs(r,c)
                

        return nIslands