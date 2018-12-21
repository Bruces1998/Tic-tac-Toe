def board(a):
    '''
    INPUT : A list containing 9 elements.
    OUTPUT: The 9 elements of the list will be positioned as given in the code below. 
    '''
    print(a[7]+'| '+a[8]+' |'+a[9])
    print('_|___|_ ')
    print(' |   |  ')
    print(a[4]+'| '+a[5]+' |'+a[6])
    print('_|___|_ ')
    print(' |   |  ')
    print(a[1]+'| '+a[2]+' |'+a[3])
c=0
bo=[' ',' ',' ',' ',' ',' ',' ',' ',' ',' ']
print('Welcome TO Tic-Tac-Toe')
sel=input('Player 1 Enter Your Choice:')
'''
Player 1's choice is taken
and accordingly player 2 is 
assigned the other choice.
'''
if(sel=='X'):
    rem='O'
else:
    rem='X'
print(sel,rem)





while(c<=9):
    '''
    This loop will keep the game running 
    and will keep updating the board after 
    every player input.
    The loop terminates if the game is over
    and the player wishes not to continue the 
    game.
    '''
    board(bo)
    print('         ')
    
    
    
    y=int(input('PLay'))
    bo[y]=sel
    c=c+1
    board(bo)
    print('         ')
    if(bo[1]==bo[2]==bo[3]==sel or
       bo[4]==bo[5]==bo[6]==sel or
       bo[7]==bo[8]==bo[9]==sel or
       bo[1]==bo[4]==bo[7]==sel or
       bo[2]==bo[8]==bo[5]==sel or
       bo[3]==bo[6]==bo[9]==sel or
       bo[7]==bo[5]==bo[3]==sel or
       bo[1]==bo[5]==bo[9]==sel):
        
        
        print('Player 1 wins')
        choice=input('Want a regame?-Y or N')
        if(choice=='Y'):
                c=0
                bo=[' ',' ',' ',' ',' ',' ',' ',' ',' ',' ']
                continue
        else:
                break
    

    if(c==9):
        print('MATCH DRAW')
        choice=input('Want a regame?-Y or N')
        if(choice=='Y'):
                c=0
                bo=[' ',' ',' ',' ',' ',' ',' ',' ',' ',' ']
                continue
        else:
                break
    
    z=int(input('PLay'))
    bo[z]=rem
    c=c+1
    board(bo)
    print('         ')
    
    
    
    if(bo[1]==bo[2]==bo[3]==rem or
       bo[4]==bo[5]==bo[6]==rem or
       bo[7]==bo[8]==bo[9]==rem or
       bo[1]==bo[4]==bo[7]==rem or
       bo[2]==bo[8]==bo[5]==rem or
       bo[3]==bo[6]==bo[9]==rem or
       bo[7]==bo[5]==bo[3]==rem or
       bo[1]==bo[5]==bo[9]==rem):
        
        
        print('Player 2 wins')
        choice=input('Want a regame?-Y or N')
        if(choice=='Y'):
                c=0
                bo=[' ',' ',' ',' ',' ',' ',' ',' ',' ',' ']
                continue
        else:
                break