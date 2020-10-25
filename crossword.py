def isVertical(grid,y,x):
    isvertical=False
    #top check
    if y==0:
        isvertical=True
    elif grid[y-1][x] == '#':
        
        isvertical=True
    if isvertical==True and y+2<len(grid):
        if grid[y][x]== '.' and grid[y+1][x]== '.' and grid[y+2][x]== '.':
            isvertical=True
        else:
            isvertical=False
    else:
        isvertical=False
    return isvertical

def isHorizontal(grid,y,x):
    ishorizontal=False
    #sidecheck AAAAAAAA
    if x==0:
        ishorizontal=True
    elif grid[y][x-1] == '#':
        ishorizontal=True
        
    if ishorizontal==True and x+2<len(grid[y]):
        if grid[y][x]== '.' and grid[y][x+1]== '.' and grid[y][x+2]== '.':
            ishorizontal=True
        else:
            ishorizontal=False
    else:ishorizontal=False
    return ishorizontal

w,l=input().split()
w,l=int(w),int(l)
grid=[]
correctpos=[]
for counter1 in range(w):
    temp=input()
    temp1=[]
    for c in range(len(temp)):
        temp1.append(temp[c])
    grid.append(temp1)
    
#main loop fkfcjf3rh
for y in range(w):
    for x in range(l):
        if isVertical(grid,y,x)==True or isHorizontal(grid,y,x)==True:
            xz=(y+1,x+1)
            correctpos.append(xz)
print(len(correctpos))
for i in range(len(correctpos)):
    print(correctpos[i][0],correctpos[i][1])

    
            
    
        
        
    