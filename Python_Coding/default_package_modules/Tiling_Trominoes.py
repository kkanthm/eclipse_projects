'''
Created on Feb 12, 2019
@author: Krishnakanth Mamidipelly L20469472
COSC 5313 Program #2
Tiling Problem
Divide and Conquer Algorithm
The program is producing the expected correct outputs
'''
from collections import namedtuple
def tilingTrominoes(n,location,missing,trominoesList):
    if n==2:
            #The 2X2 box , filling that square with a single Tromino
        if missing.x==location.x:
            if missing.y==location.y:
                trominoesList.append(Tromino(location,0))
                  
            if missing.y==location.y+1:
                trominoesList.append(Tromino(location,1))
                
        elif missing.y==location.y:
            if missing.x==location.x+1:
                trominoesList.append(Tromino(location,3))
               
        if missing.x==location.x+1 and missing.y==location.y+1:
            trominoesList.append(Tromino(location,2))
            
        return;
        
    # Need to find l1-l4 and m1-m4 and appending the center tromino
    m1,m2,m3,m4 = None,None,None,None; #Initializing all the missing squares
    center = Point(location.x+n//2,location.y+n//2)
    l1,l2,l3,l4 = location, Point(location.x,center.y), center, Point(center.x,location.y);
    if missing.x<center.x: 
        if missing.y<center.y: #0 Quadrant
            trominoesList.append(Tromino(Point(center.x-1,center.y-1),0));
            
            m1,m2,m3,m4 = missing, Point(center.x-1,center.y), center, Point(center.x,center.y-1)
      
        else: #1 Quadrant
            trominoesList.append(Tromino(Point(center.x-1,center.y-1),1));
           
            m1,m2,m3,m4 = Point(center.x-1,center.y-1), missing, center, Point(center.x,center.y-1)
        
    elif missing.x>=center.x:
        if missing.y>=center.y: #2 Quadrant
            trominoesList.append(Tromino(Point(center.x-1,center.y-1),2));
            
            m1,m2,m3,m4 = Point(center.x-1,center.y-1), Point(center.x-1,center.y), missing, Point(center.x,center.y-1)
      
        else: #3 Quadrant
            trominoesList.append(Tromino(Point(center.x-1,center.y-1),3));
            
            m1,m2,m3,m4 = Point(center.x-1,center.y-1), Point(center.x-1,center.y), center, missing
          
    tilingTrominoes(n//2, l1, m1, trominoesList)
    tilingTrominoes(n//2, l2, m2, trominoesList)
    tilingTrominoes(n//2, l3, m3, trominoesList)
    tilingTrominoes(n//2, l4, m4, trominoesList)

Point = namedtuple('Point','x y');
Tromino = namedtuple('Tromino', 'position q')
inputcases = [[4,Point(3,3)],[8,Point(4,5)],[8,Point(4,4)],[16,Point(0,0)]];
print();print()
inputCount=1;
for each in inputcases:
    trominoesList=[]
    n=each[0];
    Origin = Point(0,0);
    missingSquare = each[1];
    print('INPUT COUNT:: {}'.format(inputCount))
    print('\tBOARD SIZE: {}'.format(n))
    print('\tLOCATION AT: {} AND {}'.format(Origin.x,Origin.y));
    print('\tMISSING SQUARE AT: {} AND {}'.format(missingSquare.x,missingSquare.y));
    print('\tTOTAL OF TROMINOES COMPUTED::: {}'.format(((n*n)-1)//3))
    print()
    print('ALL TROMINOES FOLLOW:::')
    #Need to implement Function Code
    tilingTrominoes(n,Origin,missingSquare,trominoesList)
    trominoesList.sort()
    ind = 1;
    for eachTromino in trominoesList:
        print('\t {:2d}: (({:2d}, {:2d}), {:2d})'.format(ind,eachTromino[0].x,eachTromino[0].y,eachTromino[1]))
        ind=ind+1;
    
    print()
    print()
    inputCount=inputCount+1;


  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
    
    






