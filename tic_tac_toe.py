#Aristeidis Moustakas AEM: 2380

import random

def printTable(): ##prints the current table.
    print()
    for i in range(3):
        print(pin[0+i*3],pin[1+i*3],pin[2+i*3],"                  ",1+3*i,2+3*i,3+3*i)
    print()

def checkIfPlayIsDone(pin): ##Takes as argument one list and checks if the game is over in that list(table).
    p=freePos() 
    for i in range(0,3):
        if pin[0+i*3]==pin[1+i*3] and pin[1+i*3]==pin[2+i*3] and pin[0+i*3]!='_': ##checks lines
            return pin[0+i*3]
        if pin[0+i]==pin[3+i] and pin[3+i]==pin[6+i] and pin[0+i]!='_': ##checks columns 
            return pin[0+i]
    if pin[0]==pin[4] and pin[4]==pin[8]and pin[0]!='_' : ##checks diagonial
        return pin[0]
    elif pin[2]==pin[4] and pin[4]==pin[6]and pin[2]!='_' :  
        return pin[2]
    elif len(p)==0:
        return "Tie"
    return "cont"



def winInNextMove(): ##checks if PC can win in the next move and does this move.   
    chpin=pin[:] ## create a copy of the list "pin" and makes some tries on the copied list.
    for i in range(0,9):
        if chpin[i]==free:
            chpin[i]=pcSymbol
            answer=checkIfPlayIsDone(chpin)
            if answer==pcSymbol:
                pin[i]=pcSymbol
                return True
            else:
                chpin[i]=free
    return False

	
def iLoseInNextMove(): ##checks if PC is going to lose in the next move and does the most suitable move to stop the player.
    chpin=pin[:] ## create a copy of the list "pin" and makes some tries on the copied list.
    for i in range(0,9):
        if chpin[i]==free:
            chpin[i]=playerSymbol
            answer=checkIfPlayIsDone(chpin)
            if answer==playerSymbol:
                pin[i]=pcSymbol
                return True
            else:
                chpin[i]=free
    return False

def freePos(): # finds all the free boxes and returns a list with the numbers of these boxes.
    t=[]
    for i in range(0,9):
        if pin[i]==free:
            t.append(i)       
    return t
            


def randomMove(): ## makes a random move for the PC.
    t=freePos();
    pin[t[random.randint(0,len(pin)-1)]]=pcSymbol

	
	
	
def tryInCenter(): ## with probability 66%(if is the first PC's move ) tries to puts 'X' to the center. 
    rand=random.randint(0,2) ## If it isn't the first move puts 100% 'X' to the center(if the center is free).
    p=freePos()
    if rand==2 and len(p)==9:
        return False
    if pin[4]==free:
        pin[4]=pcSymbol
        return True
    return False

def findTheBestCorner():##Finds the best corner and put 'X' to it. More specifically each corner has a score(s0,s2,s6,s8).At start 
			## all scores are 0. The score decreases by 1, if there is at least one playerSymbol in the line in which owned the corner else
			##score increases by 3 if there is one 'X' in the line, else if the line is clear score increases by 1. The same happens
			## for the columns and diagonials(In this way, the same scores are increasing and dicreasing (s0,s2,s6,s8) ).
			## Finally PC choose the corner with the biggest score and put 'X' in that.If there isn't any free corner returns false.

	
	
    p=freePos()			##This is a special case in which player has the center box and pc has a corner and pc puts 'X' in the diagonial corner.
    if len(p)==7:		##In this case pc has big probability to win.
        if pin[0]==pcSymbol and pin[4]==playerSymbol:
            pin[8]=pcSymbol
            return True
        elif pin[8]==pcSymbol and pin[4]==playerSymbol:
            pin[0]=pcSymbol
            return True
        elif pin[2]==pcSymbol and pin[4]==playerSymbol:
            pin[6]=pcSymbol
            return True
        elif pin[6]==pcSymbol and pin[4]==playerSymbol:
            pin[2]=pcSymbol
            return True

			
		
    thereAfreeCorner=False
    s0=-1000
    if pin[0]==free:
        s0=0
        thereAfreeCorner=True
        if pin[1]==playerSymbol or pin[2]==playerSymbol:
            s0-=1
        elif pin[1]==pcSymbol or pin[2]==pcSymbol:
            s0=s0+3
        else:
            s0=s0+1
        if pin[3]==playerSymbol or pin[6]==playerSymbol:
            s0-=1
        elif pin[3]==pcSymbol or pin[6]==pcSymbol:
            s0=s0+3
        else:
            s0=s0+1
        if pin[8]==playerSymbol or pin[4]==playerSymbol:
            s0-=1
        elif pin[8]==pcSymbol or pin[4]==pcSymbol:
            s0=s0+3
        else:
            s0=s0+1


    s2=-1000
    if pin[2]==free:
        s2=0
        thereAfreeCorner=True
        if pin[0]==playerSymbol or pin[1]==playerSymbol:
            s2-=1
        elif pin[0]==pcSymbol or pin[1]==pcSymbol:
            s2=s2+3
        else:
            s2=s2+1
        if pin[4]==playerSymbol or pin[6]==playerSymbol:
            s2-=1
        elif pin[4]==pcSymbol or pin[6]==pcSymbol:
            s2=s2+3
        else:
            s2=s2+1
        if pin[8]==playerSymbol or pin[5]==playerSymbol:
            s2-=1
        elif pin[8]==pcSymbol or pin[5]==pcSymbol:
            s2=s2+3
        else:
            s2=s2+1

    s6=-1000
    if pin[6]==free:
        s6=0
        thereAfreeCorner=True
        if pin[0]==playerSymbol or pin[3]==playerSymbol:
            s6-=1
        elif pin[0]==pcSymbol or pin[3]==pcSymbol:
            s6=s6+3
        else:
            s6=s6+1
        if pin[4]==playerSymbol or pin[2]==playerSymbol:
            s6-=1
        elif pin[4]==pcSymbol or pin[2]==pcSymbol:
            s6=s6+3
        else:
            s6=s6+1
        if pin[8]==playerSymbol or pin[7]==playerSymbol:
            s6-=1
        elif pin[8]==pcSymbol or pin[7]==pcSymbol:
            s6=s6+3
        else:
            s6=s6+1

    s8=-100
    if pin[8]==free:
        s8=0
        thereAfreeCorner=True
        if pin[6]==playerSymbol or pin[7]==playerSymbol:
            s8-=1
        elif pin[6]==pcSymbol or pin[7]==pcSymbol:
            s8=s8+3
        else:
            s8=s8+1
        if pin[0]==playerSymbol or pin[4]==playerSymbol:
            s8-=1
        elif pin[0]==pcSymbol or pin[4]==pcSymbol:
            s8=s8+3
        else:
            s8=s8+1
        if pin[2]==playerSymbol or pin[5]==playerSymbol:
            s8-=1
        elif pin[2]==pcSymbol or pin[5]==pcSymbol:
            s8=s8+3
        else:
            s8=s8+1
            
    if thereAfreeCorner:
        max=-50
        c=0
        pos=0
        lista=[s0,s2,s6,s8]
        for i in lista:
            if i>=max:
                max=i
                pos=c
            c+=1
        if  pos==0:
            pin[0]=pcSymbol
        elif  pos==1:
            pin[2]=pcSymbol
        elif  pos==2:
            pin[6]=pcSymbol
        elif  pos==3:
            pin[8]=pcSymbol
        return True
    else:
        return False
    
	
	
	
	
	
	
	
	
def findNextBestPos(): ##Finds the best position ( without the corners and the center) and put 'X' to this. More specifically each box
                        ##has a score(s1,s3,s6,s8).At start all scores are 0. The score decreases 1 by if there is at least one 'O' in the line in which
                        ## owned the box else score increases by 3 if there is one 'X' in the line else if the line is clear score increases by 1.
			## The same thing happens for the columns ( the same scores are increasing and decreasing(s1,s3,s6,s8)) .Finally PC choose
			##  the box with the biggest score and put pcSymbol in that.

    thereAfreePos=False       
    s1=-1000
    if pin[1]==free:
        s1=0
        thereAfreePos=True
        if pin[0]==playerSymbol or pin[2]==playerSymbol:
            s1-=1
        elif pin[0]==pcSymbol or pin[2]==pcSymbol:
            s1=s1+2
        else:
            s1=s1+1
        if pin[4]==playerSymbol or pin[7]==playerSymbol:
            s1-=1
        elif pin[4]==pcSymbol or pin[7]==pcSymbol:
            s1=s1+2
        else:
            s1=s1+1

    s3=-1000
    if pin[3]==free:
        s3=0
        thereAfreePos=True
        if pin[0]==playerSymbol or pin[6]==playerSymbol:
            s3-=1
        elif pin[0]==pcSymbol or pin[6]==pcSymbol:
            s3=s3+2
        else:
            s3=s3+1
        if pin[4]==playerSymbol or pin[5]==playerSymbol:
            s3-=1
        elif pin[4]==pcSymbol or pin[5]==pcSymbol:
            s3=s3+2
        else:
            s3=s3+1

    s5=-1000
    if pin[5]==free:
        s5=0
        thereAfreePos=True
        if pin[2]==playerSymbol or pin[8]==playerSymbol:
            s5-=1
        elif pin[2]==pcSymbol or pin[8]==pcSymbol:
            s5=s5+2
        else:
            s5=s5+1
        if pin[4]==playerSymbol or pin[3]==playerSymbol:
            s5-=1
        elif pin[4]==pcSymbol or pin[3]==pcSymbol:
            s5=s5+2
        else:
            s5=s5+1

    s7=-1000
    if pin[7]==free:
        s7=0
        thereAfreePos=True
        if pin[6]==playerSymbol or pin[8]==playerSymbol:
            s7-=1
        elif pin[6]==pcSymbol or pin[8]==pcSymbol:
            s7=s7+2
        else:
            s7=s7+1
        if pin[4]==playerSymbol or pin[1]==playerSymbol:
            s7-=1
        elif pin[4]==pcSymbol or pin[1]==pcSymbol:
            s7=s7+2
        else:
            s7=s7+1

    if thereAfreePos:
        max=-50
        c=0
        pos=0
        lista=[s1,s3,s5,s7]
        for i in lista:
            if i>=max:
                max=i
                pos=c
            c+=1
        if  pos==0:
            pin[1]=pcSymbol
        elif  pos==1:
            pin[3]=pcSymbol
        elif  pos==2:
            pin[5]=pcSymbol
        elif  pos==3:
            pin[7]=pcSymbol
        return True
    else:
        return False

		

def playerHasTwoDangerousBoxes(): ## Checks if the player has two 'O' in two boxes (that make a dangerous combination) and makes the suitable move to stop him.If it doesn't happens this return false.
    p=freePos()
    if len(p)==6:
        if pin[0]==playerSymbol and pin[8]==playerSymbol: ##and pin[4]==pcSymbol:
            if pin[1]==free:
                pin[1]=pcSymbol
                return True
        elif pin[2]==playerSymbol and pin[6]==playerSymbol: ##and pin[4]==pcSymbol:
            if pin[7]==free:
                pin[7]=pcSymbol
                return True
        elif pin[1]==playerSymbol and pin[3]==playerSymbol:
            if pin[0]==free:
                pin[0]=pcSymbol
                return True
        elif pin[1]==playerSymbol and pin[5]==playerSymbol:
            if pin[2]==free:
                pin[2]=pcSymbol
                return True
        elif pin[5]==playerSymbol and pin[7]==playerSymbol:
            if pin[8]==free:
                pin[8]=pcSymbol
                return True
        elif pin[3]==playerSymbol and pin[7]==playerSymbol:
            if pin[6]==free:
                pin[6]=pcSymbol
                return True
    return False
    
    
        
def nextPcMove():
    
    if not winInNextMove(): ## checks PC can win in the next move and makes this move.
        if not iLoseInNextMove():  ## checks if PC is going to lose in the next move and makes the most suitable move to stop it.
            if not tryInCenter(): ##  Tries to put 'X' to the center.
                if not playerHasTwoDangerousBoxes(): ## Checks if the player has two 'O' in two boxes (that make a dangerous combination) and makes the most suitable move to stop him.
                    if not findTheBestCorner(): ## Finds the best corner and puts 'X' to it.
                        findNextBestPos() ## Finds the best pos from(2,4,6,8) and puts 'X' to it.


						
						
def newGame(firstPc): ##This loop is a new game , more specifically print the current table , asks the player for his next move 
    game=True	       ## and call the function nextPcMove() for the PC's next move.It stops only when the function checkIfPlayIsDone()
    for i in range(0,9):## return that the game is over.
        pin[i]='_'
    if(firstPc):
        nextPcMove()

    while game:
        # Player's move 'Ο'
        while True:
                printTable()
                try:
                        x = int(input('Play (1-9): '))-1
                        break
                except ValueError:
                        print('give a number between (1-9)!')
        if x<9 and x>=0: 
            if pin[x] == free :
                pin[x]=playerSymbol
            else:
                print('wrong move.play again!')
                continue
        else:
            print('give a number between (1-9)!')
            continue
            

        # Pc's move 'Χ'
        if checkIfPlayIsDone(pin)=="cont":
            nextPcMove()
         
        ans=checkIfPlayIsDone(pin)
        if ans!="cont":
            if ans==playerSymbol:
                game=False
                printTable()
                print("Well done!! You are the winner!!")
            elif ans==pcSymbol:
                printTable()
                print("You  lost. Pc is the winner. Τry again.")
                game=False
            elif ans=="Tie":
                printTable()
                print("the game has a draw.")
                game=False



				

				
pin=['_' for i in range(9)]
pcSymbol="X"
playerSymbol="O"
free="_"
newgame=True
aa="a"
while aa!="yes" and aa!="no": 
    aa = input('Do you want to play first(yes/no)?')
    aa = aa.lower()
if aa=="no":
    newGame(True)
elif aa=="yes":
    newGame(False)
    

while newgame: ## This loop creates a new game every time the player answers "yes" the question "Do you want to play again(yes/no)?'"  
    aa="a"	##and stops when the player answers "no".
    while aa!="yes" and aa!="no": 
        aa = input('Do you want to play again(yes/no)?')
        aa = aa.lower()
    if aa=="no":
        newgame=False
    elif aa=="yes":
        newgame=True
        aaq="a"
        while aaq!="yes" and aaq!="no": 
            aaq = input('Do you want to play first(yes/no)?')
            aaq = aaq.lower()
            if aaq=="no":
                newGame(True)
            elif aaq=="yes":
                newGame(False)    

