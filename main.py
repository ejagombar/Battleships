import random
from re import T
import os

clear = lambda: os.system('cls')


print("main")

class Player():

    

    def __init__(self,size,shipNum,name=""):
        self.name = name
        self.size = size
        self.shipNum = shipNum
        self.myGrid = [[0 for x in range(self.size)] for y in range(self.size)]
        self.shipList = []
        self.__PlaceShips(self.shipNum)
        
    def Get_myGrid(self):
        return self.myGrid

    def Bomb(self,xPos,yPos):
        
        tile = self.myGrid[xPos][yPos]

        if (tile == 0) or (tile == -1) or (tile == -2):
            self.myGrid[xPos][yPos] = -1
            return -1
        else:
            print(tile)
            self.myGrid[xPos][yPos] = -2
            if self.shipList[int(tile)-1].hitAndDestroyed():
                return -2
            else:
                return -3
        



    def __PlaceShips(self,shipNum):
        for ship in range(1,shipNum+1):
            
            shipLength = random.randint(3,5)
            direction = random.randint(0,1)

            while True:
                valid = True
                xpos,ypos = random.randint(0,self.size-shipLength), random.randint(0,self.size-shipLength)
                for j in range(shipLength):
                    if self.myGrid[xpos+(j*direction)][ypos+(j*(1-direction))] != 0:
                        valid = False
                if valid == True:
                    break

            for j in range(shipLength):
                self.myGrid[xpos+(j*direction)][ypos+(j*(1-direction))] = ship


            shipInArray = Battleship(xpos,ypos,direction,shipLength)
            self.shipList.append(shipInArray)
            #print(self.shipList[self.shipNum-1].hitAndDestroyed())
    def __AddExtraIndent(self):
        if self.size > 10:
            print(" ",end="")
       


    def DisplayGrid(self,grid,defence):

        if self.size > 10:
            print("\n   ",end="")
            for i in range(self.size):
                print(str(i//10)+" ",end='')
            print("  ",end="")

        print("\n  ",end="")
        self.__AddExtraIndent()

        for i in range(self.size):
            print(str(i%10)+" ",end='')
            
        self.__AddExtraIndent()
        print(" \n ",end="")
        self.__AddExtraIndent()

        print("\N{FULL BLOCK}"*(self.size*2+1))

        for i in range(self.size):
            if self.size > 10:
                print("%02d" % i,end='')
            else:
                print("%01d" % i,end='')
            print("\N{FULL BLOCK}",end="")

            for j in range(self.size):

                if (grid[i][j] > 0) and defence:
                    print(""+str(grid[i][j])+"",end="")
                elif (grid[i][j] < 0):

                    if grid[i][j] == -1:
                        print("~",end="")
                    if grid[i][j] == -2:
                        print("x",end="")     
                else:
                    print(" ",end="") 


                if j < self.size-1:
                    print("|",end="")

            print("\N{FULL BLOCK}")

        self.__AddExtraIndent()
        print(" ",end="")
        print("\N{FULL BLOCK}"*(self.size*2+1))
        
class Battleship():

    def __init__(self,xpos,ypos,direction,shipLength):
        self.xpos = xpos
        self.ypos = ypos
        self.direction = direction
        self.shipLength = shipLength
        self.damage = 0
    
    def hitAndDestroyed(self):
        self.damage += 1
        if self.damage == self.shipLength:
            return True
        else:
            return False


class Game():

    def __init__(self):
        self.player1 = Player(10,5)
        self.player2 = Player(10,5)

        self.setup()
        self.getplayerNames()
        self.tutorial(self.player1, self.player2)
    
    def setup(self):
        clear()
        print("\N{FULL BLOCK}"*27)
        print("\N{FULL BLOCK} Welcome to Battleships! \N{FULL BLOCK}")
        print("\N{FULL BLOCK}"*27)
        input("\n  Press enter to start")
        clear()


    def getplayerNames(self):
        
        name = input("Please enter the name of player 1: ")
        self.player1.name = name
        name = input("Please enter the name of player 2: ")
        self.player2.name = name

    def tutorial(self,player1,player2):

        input("\n It is "+str(player1.name)+"'s go. Press enter to start")
        clear()

        player1.DisplayGrid(player1.Get_myGrid(),True)
        print("\nHere is your battleship map. You have "+str(player1.shipNum)+" battleships")
        input("Do not give away your battleship locations to "+str(player2.name))

        self.player2.DisplayGrid(player2.Get_myGrid(),False)
        print("\nHere is " + str(player2.name) + "'s map.")
        print("Their ships do not appear on your radar however they need to be destroyed.")
        print("Chose a location on the grid to send a missile\n")

        self.playerShoot(player2)

        input("\n Press enter to continue")



    def playerShoot(self,player):
        xInput = int(input("X Coordinate: "))
        yInput = int(input("Y Coordinate: "))

        result = player.Bomb(yInput,xInput)

        print("")

        if result == -1:
            print("Missed!")
        elif result == -3:
            print("Hit!")
        elif result == -2:
            print("Hit and Destroyed!")


game = Game()
