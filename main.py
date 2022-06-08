import random
from re import T

print("main")

class player():

    def __init__(self,size,name):
        self.name = name
        self.size = size
        self.myGrid = [[0 for x in range(self.size)] for y in range(self.size)]
        self.guessGrid = [[0 for x in range(self.size)] for y in range(self.size)]
        self.__PlaceShips(5)
        

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


    def __AddExtraIndent(self):
        if self.size > 10:
            print(" ",end="")


    def DisplayGrid(self):

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
                if self.myGrid[i][j] == 0:
                   print(" ",end="") 
                else:
                    print(""+str(self.myGrid[i][j])+"",end="")

                if j < self.size-1:
                    print("|",end="")

            print("\N{FULL BLOCK}")

        self.__AddExtraIndent()
        print(" ",end="")
        print("\N{FULL BLOCK}"*(self.size*2+1))
        

x = player(10,"salma")

x.DisplayGrid()



