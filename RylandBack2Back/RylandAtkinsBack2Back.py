#Ryland Atkins
#This is entirely my own work.
#I used stack exchange to learn how to use rot90.

from Tkinter import *
import numpy as np


"""I'm turning in what I have because I want you to know that I've been working on it,
but I think that I bit off more than I can chew with the GUI. Currently, the features I lack:
-Placing pieces that overlap
-A bug that restricts what part of the piece shows up after the rotation
-An uncaught index out of bounds exception when placing certain pieces
-Graphic detail on the pieces to make their orientation clear before placing
-Endgame
I think that's all at the moment. I'll speak to you today in class about it.
"""
class b2bGUI(Frame):

    """
    GUI representation of the back to back game. The game is mirrored in the
    middle, so that the top right circle on the right board correlates to the
    top left circle on the left board and so on.
    """
    def setTop(self):
        print "setting top"
        
        for k in self.pieceList:
            if k.getInHome():
                for i in range(k.getFront().shape[0]):
                    for j in range(k.getFront().shape[1]):
                        if k.getFront()[i][j] == 1:
                            I = k.getHomeCoords()[0]
                            J = k.getHomeCoords()[1]
                            circ = ((9+88*I+j*88),(4+69*J+i*69),
                                    (79+88*I+j*88),(64+69*J+i*69))
                            self.pieces.create_oval(circ,fill=k.getColor())
                
                

    def fillCircle(self,side,circle,color,fullness):
        """
        Circles are defined by their cartesian coordinates --from (0,0)
        to (5,4);(i,j)-- and their side --either 'front' or 'back'. 
        """
        if side == 'front':
            side = self.front
        elif side == 'back':
            side = self.back
        elif side == self.pieces:
            return
            
        empty = "lightgray"
        if(fullness == 1):
            outCoords=((10+100*circle[0]),(10+100*circle[1]),(90+100*circle[0]),
                       (90+100*circle[1]))
            whtCoords=((15+100*circle[0]),(15+100*circle[1]),(85+100*circle[0]),
                       (85+100*circle[1]))
            inCoords=((20+100*circle[0]),(20+100*circle[1]),(80+100*circle[0]),
                       (80+100*circle[1]))
            side.create_oval(outCoords,fill=color)
            side.create_oval(whtCoords,fill="white")
            side.create_oval(inCoords,fill=color)
        elif(fullness == 0):
            outCoords=((10+100*circle[0]),(10+100*circle[1]),(90+100*circle[0]),
                       (90+100*circle[1]))
            side.create_oval(outCoords,fill=empty)
        elif(fullness == 2):
            outCoords=((10+100*circle[0]),(10+100*circle[1]),(90+100*circle[0]),
                       (90+100*circle[1]))
            side.create_oval(outCoords,fill=color)

    def isFull(self,side,circle):
        if side == self.front:
            return (self.front[circle[0]][circle[1]]==1)
        else:
            return (self.back[circle[0]][circle[1]]==1)
            

    def select(self,x,y):

        self.pieces.delete("all")
        self.selectX = x
        self.selectY = y
        self.pieces.create_rectangle(0,0,1235,405,fill="darkgray")
        for i in range(14):
            for j in range(6):
                if((x>0)&(x<264)&(y>0)&(y<207)):
                    self.pieces.create_rectangle(0,0,264,207,fill="lightgray")
                    self.selectedPiece = self.piece5
                elif((x>264)&(x<441)&(y>0)&(y<207)):
                    self.pieces.create_rectangle(264,0,441,207,fill="lightgray")
                    self.selectedPiece = self.piece2
                elif((x>441)&(x<706)&(y>0)&(y<207)):
                    self.pieces.create_rectangle(441,0,706,207,fill="lightgray")
                    self.selectedPiece = self.piece8
                elif((x>706)&(x<884)&(y>0)&(y<207)):
                    self.pieces.create_rectangle(706,0,884,207,fill="lightgray")
                    self.selectedPiece = self.piece1
                elif((x>884)&(x<1235)&(y>0)&(y<207)):
                    self.pieces.create_rectangle(884,0,1149,207,fill="lightgray")
                    self.selectedPiece = self.piece10

                elif((x>0)&(x<264)&(y>207)&(y<405)):
                    self.pieces.create_rectangle(0,207,264,405,fill="lightgray")
                    self.selectedPiece = self.piece6
                elif((x>264)&(x<441)&(y>207)&(y<405)):
                    self.pieces.create_rectangle(264,207,441,405,fill="lightgray")
                    self.selectedPiece = self.piece3
                elif((x>441)&(x<706)&(y>207)&(y<405)):
                    self.pieces.create_rectangle(441,207,706,405,fill="lightgray")
                    self.selectedPiece = self.piece9
                elif((x>706)&(x<884)&(y>207)&(y<405)):
                    self.pieces.create_rectangle(706,207,884,405,fill="lightgray")
                    self.selectedPiece = self.piece4
                elif((x>884)&(x<1235)&(y>207)&(y<405)):
                    self.pieces.create_rectangle(884,207,1149,405,fill="lightgray")
                    self.selectedPiece = self.piece11

        self.updateGUI()

    def placePiece(self,event,x,y):
        if (self.selectedPiece.getInHome()):
            print "over here"
            if event.widget==self.front:
                try:
                    for i in range(self.selectedPiece.getFront().shape[0]):
                        for j in range(self.selectedPiece.getFront().shape[0]):
                            self.frontArray[x+i][y+j]
                            self.backArray[x+i][5-(y+j)]
                except:
                    print "Wrong move"
                    return

                for i in range(self.selectedPiece.getFront().shape[0]):
                    for j in range(self.selectedPiece.getFront().shape[0]):
                        self.frontPieces[x+i][y+j].setColor(self.selectedPiece.getColor())
                        self.frontArray[x+i][y+j] = self.selectedPiece.getFront()[i][j]
                            
                for i in range(self.selectedPiece.getBack().shape[0]):
                    for j in range(self.selectedPiece.getBack().shape[0]):
                            #T=(6*(y+j)+(x+i))
                        self.backPieces[x+i][5-(y+j)].setColor(self.selectedPiece.getColor())
                        self.backArray[x+i][5-(y+j)] = self.selectedPiece.getBack()[i][j]

            else:
                try:
                    for i in range(self.selectedPiece.getFront().shape[0]):
                        for j in range(self.selectedPiece.getFront().shape[0]):
                            self.frontArray[x+i][5-(y+j)]
                            self.backArray[x+i][y+j]
                except:
                    print "Wrong move"
                    return
                for i in range(self.selectedPiece.getFront().shape[0]):
                    for j in range(self.selectedPiece.getFront().shape[0]):
                        #T=(6*(y+j)+(x+i))
                        #R=((5-(T%6))+(((T-(T%6))%5)*6))
                        self.frontPieces[x+i][5-(y+j)].setColor(self.selectedPiece.getColor())
                        self.frontArray[x+i][5-(y+j)] = self.selectedPiece.getBack()[i][j]
                        
                for i in range(self.selectedPiece.getBack().shape[0]):
                    for j in range(self.selectedPiece.getBack().shape[0]):
                        #T=(6*(y+j)+(x+i))
                        self.backPieces[x+i][y+j].setColor(self.selectedPiece.getColor())
                        self.backArray[x+i][y+j] = self.selectedPiece.getFront()[i][j]                

        self.selectedPiece.setInHome(False)
        self.updateGUI()

               
    def callback(self,event):
        """What to do if a click occurs"""
        print "clicked at ",event.x,event.y
        if (event.widget!=self.pieces):
            for i in range(5):
                for j in range(6):
                    if(((event.x > (10+100*j))&(event.x < (90+100*j)))&
                       ((event.y > (10+100*i))&(event.y < (90+100*i)))):
                       
                        self.placePiece(event,i,j)
                        
        else:
            self.select(event.x,event.y)
        return True

    def checkClear(self,location):
        t=5

    
    def updateGUI(self):
        #for front and back side

        
        I=0
        for i in self.frontArray:
            J=0
            for j in i:
                self.fillCircle('front',(J,I),self.frontPieces[I][J].getColor(),j)
                J=J+1
            I=I+1

        I=0
        for i in self.backArray:
            J=0
            for j in i:
                self.fillCircle('back',(J,I),self.backPieces[I][J].getColor(),j)
                J=J+1
            I=I+1


        #for top box       
        for i in range(14):
            self.pieces.create_line(88*i,0,88*i,405)
        for j in range(6):
            self.pieces.create_line(0,69*j,1235,69*j)
        
        self.setTop()
        print self.frontArray
                
    def reset(self):
        self.pieces.delete("all")
        self.front.delete("all")
        self.back.delete("all")

        for i in range(14):
            self.pieces.create_line(88*i,0,88*i,405)
        for j in range(6):
            self.pieces.create_line(0,69*j,1235,69*j)
                

        self.frontArray = np.array([[0,0,0,0,0,0],
                                    [0,0,0,0,0,0],
                                    [0,0,0,0,0,0],
                                    [0,0,0,0,0,0],
                                    [0,0,0,0,0,0]], int)

        self.frontPieces = []
        for i in range(5):
            self.frontPieces.append([])
            for j in range(6):
                self.frontPieces[i].append(b2bPiece("lightgray",[[0]],[[0]],(-1,-1)))

        self.backArray  = np.array([[0,0,0,0,0,0],
                                    [0,0,0,0,0,0],
                                    [0,0,0,0,0,0],
                                    [0,0,0,0,0,0],
                                    [0,0,0,0,0,0]], int)

        self.backPieces = []
        for j in range(5):
            self.backPieces.append([])
            for i in range(6):
                self.backPieces[j].append(b2bPiece("lightgray",[[0]],[[0]],(-1,-1)))

        
        piece1 =(np.array([[1,1],
                           [1,0]], int),
                 np.array([[2,1],
                           [1,0]], int))
        self.piece1 = b2bPiece("darkgreen",piece1[0],piece1[1],(8,0))
        self.pieceList = [self.piece1]
        piece2 =(np.array([[1,1],
                           [1,0]], int),
                 np.array([[1,1],
                           [2,0]], int))
        self.piece2 = b2bPiece("pink",piece2[0],piece2[1],(3,0))
        self.pieceList.append(self.piece2)
        piece3 =(np.array([[1,1],
                           [1,0]], int),
                 np.array([[1,1],
                           [2,0]], int))
        self.piece3 = b2bPiece("pink",piece3[0],piece3[1],(3,3))
        self.pieceList.append(self.piece3)
        piece4 =(np.array([[1,1],
                           [1,0]], int),
                 np.array([[1,1],
                           [2,0]], int))
        self.piece4 = b2bPiece("darkblue",piece4[0],piece4[1],(8,3))
        self.pieceList.append(self.piece4)
        piece5 =(np.array([[1],
                           [1],
                           [1]], int),
                 np.array([[1],
                           [2],
                           [1]], int))
        self.piece5 = b2bPiece("lightblue",piece5[0],piece5[1],(0,0))
        self.pieceList.append(self.piece5)
        piece6 =(np.array([[1],
                           [1],
                           [1]], int),
                 np.array([[2],
                           [1],
                           [1]], int))
        self.piece6 = b2bPiece("red",piece6[0],piece6[1],(0,3))
        self.pieceList.append(self.piece6)
        piece7 =(np.array([[1,1],
                           [1,0],
                           [1,0]], int),
                 np.array([[1,2],
                           [2,0],
                           [1,0]], int))
        self.piece7 = b2bPiece("darkgreen",piece7[0],piece7[1],(-1,-1))
        self.pieceList.append(self.piece7)
        piece8 =(np.array([[1,0],
                           [1,1],
                           [1,0]], int),
                 np.array([[2,0],
                           [1,2],
                           [1,0]], int))
        self.piece8 = b2bPiece("yellow",piece8[0],piece8[1],(5,0))
        self.pieceList.append(self.piece8)
        piece9 =(np.array([[1,0],
                           [1,1],
                           [0,1]], int),
                 np.array([[2,0],
                           [2,1],
                           [0,1]], int))
        self.piece9 = b2bPiece("violet",piece9[0],piece9[1],(5,3))
        self.pieceList.append(self.piece9)
        piece10 =(np.array([[1,1],
                            [0,1],
                            [0,1]], int),
                  np.array([[2,1],
                            [0,2],
                            [0,1]], int))
        self.piece10 = b2bPiece("orange",piece10[0],piece10[1],(10,0))
        self.pieceList.append(self.piece10)
        piece11 =(np.array([[1,1],
                            [0,1],
                            [0,1]], int),
                  np.array([[1,2],
                            [0,2],
                            [0,1]], int))
        
        self.piece11 = b2bPiece("green",piece11[0],piece11[1],(10,3))
        self.pieceList.append(self.piece11)
        
        self.selectedPiece = self.pieceList[0]
        self.selectX = 0
        self.selectY = 0

        self.updateGUI()
        

    def rotatePiece(self):
        print self.selectedPiece.getFront()
        self.selectedPiece.rotate()
        print self.selectedPiece.getFront()
        self.select(self.selectX,self.selectY)
        self.updateGUI()


    def createWidgets(self):
        self.QUIT = Button(self)
        self.QUIT["text"] = "QUIT"
        self.QUIT["fg"]   = "red"
        self.QUIT["command"] =  self.quit

        self.QUIT.pack({"side": "left"})

        self.RESET = Button(self)
        self.RESET["text"] = "RESET",
        self.RESET["command"] =  self.reset

        self.RESET.pack({"side": "left"})

        self.rotate = Button(self)
        self.rotate["text"] = "ROTATE"
        self.rotate["command"] = self.rotatePiece

        self.rotate.pack({"side": "left"})


    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.pack()
        self.createWidgets()

        master.title("Back2Back")
        master.minsize(width=1250,height=800)

        self.pieces = Canvas(master,bd=3,bg="darkgray",height=400,width=1200,relief=GROOVE)
        self.pieces.bind("<Button-1>", self.callback)
        self.pieces.pack(expand=True,anchor=S,fill=X,padx=10,pady=10)

        self.front = Canvas(master,bd=3,bg="gray",height=500,width=600,relief=GROOVE)
        self.front.bind("<Button-1>", self.callback)
        self.front.pack(side="left",expand=True,anchor=NW,padx=10,pady=10)

        self.back = Canvas(master,bd=3,bg="gray",height=500,width=600,relief=GROOVE)
        self.back.bind("<Button-1>", self.callback)
        self.back.pack(side="right",expand=False,anchor=NE,padx=10,pady=10)

        for i in range(14):
            self.pieces.create_line(88*i,0,88*i,405)
        for j in range(6):
            self.pieces.create_line(0,69*j,1235,69*j)
                

        self.frontArray = np.array([[0,0,0,0,0,0],
                                    [0,0,0,0,0,0],
                                    [0,0,0,0,0,0],
                                    [0,0,0,0,0,0],
                                    [0,0,0,0,0,0]], int)

        self.frontPieces = []
        for i in range(5):
            self.frontPieces.append([])
            for j in range(6):
                self.frontPieces[i].append(b2bPiece("lightgray",[[0]],[[0]],(-1,-1)))

        self.backArray  = np.array([[0,0,0,0,0,0],
                                    [0,0,0,0,0,0],
                                    [0,0,0,0,0,0],
                                    [0,0,0,0,0,0],
                                    [0,0,0,0,0,0]], int)

        self.backPieces = []
        for j in range(5):
            self.backPieces.append([])
            for i in range(6):
                self.backPieces[j].append(b2bPiece("lightgray",[[0]],[[0]],(-1,-1)))

        
        piece1 =(np.array([[1,1],
                           [1,0]], int),
                 np.array([[2,1],
                           [1,0]], int))
        self.piece1 = b2bPiece("darkgreen",piece1[0],piece1[1],(8,0))
        self.pieceList = [self.piece1]
        piece2 =(np.array([[1,1],
                           [1,0]], int),
                 np.array([[1,1],
                           [2,0]], int))
        self.piece2 = b2bPiece("pink",piece2[0],piece2[1],(3,0))
        self.pieceList.append(self.piece2)
        piece3 =(np.array([[1,1],
                           [1,0]], int),
                 np.array([[1,1],
                           [2,0]], int))
        self.piece3 = b2bPiece("pink",piece3[0],piece3[1],(3,3))
        self.pieceList.append(self.piece3)
        piece4 =(np.array([[1,1],
                           [1,0]], int),
                 np.array([[1,1],
                           [2,0]], int))
        self.piece4 = b2bPiece("darkblue",piece4[0],piece4[1],(8,3))
        self.pieceList.append(self.piece4)
        piece5 =(np.array([[1],
                           [1],
                           [1]], int),
                 np.array([[1],
                           [2],
                           [1]], int))
        self.piece5 = b2bPiece("lightblue",piece5[0],piece5[1],(0,0))
        self.pieceList.append(self.piece5)
        piece6 =(np.array([[1],
                           [1],
                           [1]], int),
                 np.array([[2],
                           [1],
                           [1]], int))
        self.piece6 = b2bPiece("red",piece6[0],piece6[1],(0,3))
        self.pieceList.append(self.piece6)
        piece7 =(np.array([[1,1],
                           [1,0],
                           [1,0]], int),
                 np.array([[1,2],
                           [2,0],
                           [1,0]], int))
        self.piece7 = b2bPiece("darkgreen",piece7[0],piece7[1],(-1,-1))
        self.pieceList.append(self.piece7)
        piece8 =(np.array([[1,0],
                           [1,1],
                           [1,0]], int),
                 np.array([[2,0],
                           [1,2],
                           [1,0]], int))
        self.piece8 = b2bPiece("yellow",piece8[0],piece8[1],(5,0))
        self.pieceList.append(self.piece8)
        piece9 =(np.array([[1,0],
                           [1,1],
                           [0,1]], int),
                 np.array([[2,0],
                           [2,1],
                           [0,1]], int))
        self.piece9 = b2bPiece("violet",piece9[0],piece9[1],(5,3))
        self.pieceList.append(self.piece9)
        piece10 =(np.array([[1,1],
                            [0,1],
                            [0,1]], int),
                  np.array([[2,1],
                            [0,2],
                            [0,1]], int))
        self.piece10 = b2bPiece("orange",piece10[0],piece10[1],(10,0))
        self.pieceList.append(self.piece10)
        piece11 =(np.array([[1,1],
                            [0,1],
                            [0,1]], int),
                  np.array([[1,2],
                            [0,2],
                            [0,1]], int))
        self.piece11 = b2bPiece("green",piece11[0],piece11[1],(10,3))
        self.pieceList.append(self.piece11)
        
        self.selectedPiece = self.pieceList[0]
        self.selectX = 3
        self.selectY = 0

        self.updateGUI()
        
class b2bPiece:

    def __init__(self,color,frontShape,backShape,homeCoords):

        self.color = color
        self.frontShape = frontShape
        self.backShape = backShape
        self.inHome =True
        self.homeCoords = homeCoords

    def rotate(self):

        self.frontShape = np.rot90(self.frontShape)
        self.backShape = np.rot90(self.backShape)
        return

    def flip(self):
        temp = self.frontShape
        self.frontShape = self.backShape
        self.backShape = temp
        return
    def setFront(self,num):
        self.frontShape[0][0] = num

    def getFrontNum(self):
        return self.frontShape[0][0]
        
    def getFront(self):
        return self.frontShape
    
    def setBack(self,num):
        self.backShape[0][0] = num
        print self.backShape[0][0]

    def getBackNum(self):
        return self.backShape[0][0]

    def getBack(self):
        return self.backShape

    def setColor(self,color):
        self.color=color
        
    def getColor(self):
        return self.color

    def setInHome(self,inHome):
        self.inHome = inHome

    def getInHome(self):
        return self.inHome

    def getHomeCoords(self):
        return self.homeCoords
    
##
##class b2bTextBased:
##
##    def __init__(self):
##        self.frontArray = np.array([[0,0,0,0,0,0],
##                                    [0,0,0,0,0,0],
##                                    [0,0,0,0,0,0],
##                                    [0,0,0,0,0,0],
##                                    [0,0,0,0,0,0]], int)
##        self.backArray = np.array([[0,0,0,0,0,0],
##                                   [0,0,0,0,0,0],
##                                   [0,0,0,0,0,0],
##                                   [0,0,0,0,0,0],
##                                   [0,0,0,0,0,0]], int)
##        piece1 =(np.array([[1,1],
##                           [1,0]], int),
##                 np.array([[1,-1],
##                           [0,1]], int))
##
##        self.piece2 =(np.array([[2,2],
##                                [2,0]], int),
##                      np.array([[2,2],
##                                [0,-1]], int))
##    
##        self.piece3 =(np.array([[3,3],
##                                [3,0]], int),
##                      np.array([[3,3],
##                                [0,-1]], int))
##        
##        self.piece4 =(np.array([[4,4],
##                                [4,0]], int),
##                      np.array([[-1,4],
##                                [0,4]], int))
##
##        self.piece5 =(np.array([[5,0],
##                                [5,0],
##                                [5,0,0]], int),
##                      np.array([[0,0,5],
##                                [0,0,-1],
##                                [0,0,5]], int))
##        
##        self.piece6 =(np.array([[6,0,0],
##                                [6,0,0],
##                                [6,0,0]], int),
##                      np.array([[0,0,-1],
##                                [0,0,6],
##                                [0,0,6]], int))
##     
##        self.piece7 =(np.array([[7,7,0],
##                                [7,0,0],
##                                [1,0,0]], int),
##                      np.array([[0,-1,1],
##                                [0,0,-1],
##                                [0,0,1]], int))
## 
##        self.piece8 =(np.array([[1,0,0],
##                                [1,1,0],
##                                [1,0,0]], int),
##                      np.array([[0,0,-1],
##                                [0,-1,1],
##                                [0,0,1]], int))
##
##        self.piece9 =(np.array([[1,0,0],
##                                [1,1,0],
##                                [0,1,0]], int),
##                      np.array([[0,0,-1],
##                                [0,1,-1],
##                                [0,1,0]], int))
##
##        self.piece10 =(np.array([[1,1,0],
##                                [0,1,0],
##                                [0,1,0]], int),
##                      np.array([[0,1,-1],
##                                [0,-1,0],
##                                [0,1,0]], int))
##
##        self.piece11 =(np.array([[1,1,0],
##                                 [0,1,0],
##                                 [0,1,0]], int),
##                       np.array([[0,-1,1],
##                                 [0,-1,0],
##                                 [0,1,0]], int))      
##    def printSides(self):
##        for j in range(5):
##            line = ""
##            for i in range(6):
##                line = line+str(self.frontArray[j][i])
##            print line
##
##        print "\n"
##
##        for j in range(5):
##            line = ""
##            for i in range(6):
##                line = line+str(self.backArray[j][i])
##            print line

def main():

    
    root = Tk()
    app = b2bGUI(master=root)
    app.mainloop()
    root.destroy()

    #b2b = b2bTextBased()
    #b2b.printSides()

main()
