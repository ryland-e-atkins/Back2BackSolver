"""
Ryland Atkins
Back2Back GUI
This is entirely my own work.
I used stack-exchange as a resource for developing the GUI and the rot90 numpy function.
"""


from Tkinter import *
import numpy as np

class b2bGUI(Frame):

    """
    GUI representation of the back to back game. The game is mirrored in the
    middle, so that the top right circle on the right board correlates to the
    top left circle on the left board and so on.
    """
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.pack()
        self.createWidgets()

        master.title("Back2Back")
        master.minsize(width=1250,height=800)

        #Creating canvases to draw on and binding the mouse
        self.pieces = Canvas(master,bd=3,bg="darkgray",height=400,width=1200,relief=GROOVE)
        self.pieces.bind("<Button-1>", self.callback)
        self.pieces.pack(expand=True,anchor=S,fill=X,padx=10,pady=10)

        self.front = Canvas(master,bd=3,bg="gray",height=500,width=600,relief=GROOVE)
        self.front.bind("<Button-1>", self.callback)
        self.front.pack(side="left",expand=True,anchor=NW,padx=10,pady=10)

        self.back = Canvas(master,bd=3,bg="gray",height=500,width=600,relief=GROOVE)
        self.back.bind("<Button-1>", self.callback)
        self.back.pack(side="right",expand=False,anchor=NE,padx=10,pady=10)

        #Call to set up the board
        self.reset()
    
    """Used to reset the board to empty and all pieces to home location"""
    def reset(self):
        self.pieces.delete("all")
        self.front.delete("all")
        self.back.delete("all")
        
        #Lines for top section
        for i in range(14):
            self.pieces.create_line(88*i,0,88*i,405)
        for j in range(6):
            self.pieces.create_line(0,69*j,1235,69*j)
                
        
        #Arrays for board (2 per side)
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

        #Creating pieces
        piece1 =(np.array([[1,1],
                           [1,0]], int),
                 np.array([[2,1],
                           [1,0]], int))
        self.piece1 = b2bPiece("darkgreen",piece1[0],piece1[1],(6,0))
        self.pieceList = [self.piece1]
        piece2 =(np.array([[1,1],
                           [0,1]], int),
                 np.array([[1,1],
                           [0,2]], int))
        self.piece2 = b2bPiece("pink",piece2[0],piece2[1],(1,1))
        self.pieceList.append(self.piece2)
        piece3 =(np.array([[1,1],
                           [0,1]], int),
                 np.array([[1,1],
                           [0,2]], int))
        self.piece3 = b2bPiece("pink",piece3[0],piece3[1],(1,4))
        self.pieceList.append(self.piece3)
        piece4 =(np.array([[1,1],
                           [1,0]], int),
                 np.array([[1,1],
                           [2,0]], int))
        self.piece4 = b2bPiece("darkblue",piece4[0],piece4[1],(6,3))
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
        self.piece7 = b2bPiece("green",piece7[0],piece7[1],(11,0))
        self.pieceList.append(self.piece7)
        piece8 =(np.array([[1,0],
                           [1,1],
                           [1,0]], int),
                 np.array([[2,0],
                           [1,2],
                           [1,0]], int))
        self.piece8 = b2bPiece("yellow",piece8[0],piece8[1],(3,0))
        self.pieceList.append(self.piece8)
        piece9 =(np.array([[1,0],
                           [1,1],
                           [0,1]], int),
                 np.array([[2,0],
                           [2,1],
                           [0,1]], int))
        self.piece9 = b2bPiece("violet",piece9[0],piece9[1],(3,3))
        self.pieceList.append(self.piece9)
        piece10 =(np.array([[1,1],
                            [0,1],
                            [0,1]], int),
                  np.array([[2,1],
                            [0,2],
                            [0,1]], int))
        self.piece10 = b2bPiece("orange",piece10[0],piece10[1],(8,0))
        self.pieceList.append(self.piece10)
        piece11 =(np.array([[1,1],
                            [0,1],
                            [0,1]], int),
                  np.array([[1,2],
                            [0,2],
                            [0,1]], int))
        self.piece11 = b2bPiece("lightgreen",piece11[0],piece11[1],(8,3))
        self.pieceList.append(self.piece11)
        
        self.selectedPiece = self.pieceList[0]
        self.selectX = 0
        self.selectY = 0

        #Telling GUI to show everything
        self.updateGUI()        

    """Function to create buttons at the top of the window"""
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

    """Function to draw the pieces on the top Canvas"""
    def setTop(self):
        
        #
        for k in self.pieceList:
            if k.getInHome():
                for i in range(k.getFront().shape[0]):
                    for j in range(k.getFront().shape[1]):
                        if k.getBack()[i][j] == 1:
                            I = k.getHomeCoords()[0]
                            J = k.getHomeCoords()[1]
                            outCoords = ((9+88*I+j*88),(4+69*J+i*69),
                                         (79+88*I+j*88),(64+69*J+i*69))
                            whtCoords = ((12+88*I+j*88),(7+69*J+i*69),
                                         (76+88*I+j*88),(61+69*J+i*69))
                            inCoords  = ((15+88*I+j*88),(10+69*J+i*69),
                                         (73+88*I+j*88),(58+69*J+i*69))
                            self.pieces.create_oval(outCoords,fill=k.getColor())
                            self.pieces.create_oval(whtCoords,fill="white")
                            self.pieces.create_oval(inCoords,fill=k.getColor())
                        elif k.getBack()[i][j] == 2:
                            I = k.getHomeCoords()[0]
                            J = k.getHomeCoords()[1]
                            outCoords = ((9+88*I+j*88),(4+69*J+i*69),
                                         (79+88*I+j*88),(64+69*J+i*69))
                            self.pieces.create_oval(outCoords,fill=k.getColor())
            
    """Function to draw circles on the gameboard"""    
    def fillCircle(self,side,circle,color,fullness):
        """
        Circles are defined by their cartesian coordinates --from (0,0)
        to (5,4);(i,j)-- their side --either 'front' or 'back'-- their color
        and fullness--how far they stick through the board. 
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

    """Function to select and highlight a piece before placement."""
    def select(self,x,y):

        self.pieces.delete("all")
        self.selectX = x
        self.selectY = y
        self.pieces.create_rectangle(0,0,1235,405,fill="darkgray")
        I = x/88
        J = y/69
        #For every piece
        for k in self.pieceList:
            #For every circle in each piece
            for i in range(k.getFront().shape[0]):
                for j in range(k.getFront().shape[1]):
                    #if you click one of those circles, highlight and select
                    if(k.getHomeCoords()[0]+j == I)&(k.getHomeCoords()[1]+i == J):
                        self.selectedPiece = k
                        I = k.getHomeCoords()[0]
                        J = k.getHomeCoords()[1]
                        for o in range(k.getFront().shape[0]):
                            for p in range(k.getFront().shape[1]):
                                self.pieces.create_rectangle((I+p)*88,(J+o)*69,((I+p)+1)*88,((J+o)+1)*69,fill="lightgray")
                        break
        #Show pieces over highlight
        self.updateGUI()

    """Function to place a piece on the board. Pieces are place based on the upper leftmost square 
        they possess. So if you have a piece like:
        010
        111
        Where 1 represents fullness and 0 represents empty, then where you click on the board
        corresponds to where the upper left zero is placed"""
    def placePiece(self,event,x,y):
        #If the piece is in it's home, it can be placed.
        if (self.selectedPiece.getInHome()):
            #Check if placing on front or back
            #Front
            if event.widget==self.front:
                #Check if piece placement is legal
                try:
                    
                    for i in range(self.selectedPiece.getFront().shape[0]):
                        for j in range(self.selectedPiece.getFront().shape[1]):
                            #If the front or back are filled
                            if (self.frontArray[x+i][y+j] == 1)&(self.selectedPiece.getFront()[i][j] != 0):
                                print "Wrong Move1.1"
                                return
                            #If the hole is partially filled when placing a piece that goes through
                            elif ((self.frontArray[x+i][y+j] == 2)&(self.selectedPiece.getBack()[i][j] == 1)):
                                print "Wrong Move1.2"
                                return
     
                            self.frontArray[x+i][y+j]
                            self.backArray[x+i][5-(y+j)]
                except Exception,e:
                    print "Wrong Move1.3"
                    print str(e)
                    return
                #Set front
                for i in range(self.selectedPiece.getFront().shape[0]):
                    for j in range(self.selectedPiece.getFront().shape[1]):
                        if (self.selectedPiece.getFront()[i][j] == 1):
                            self.frontPieces[x+i][y+j].setColor(self.selectedPiece.getColor())
                            self.frontArray[x+i][y+j] = self.selectedPiece.getFront()[i][j]
                #Set back      
                for i in range(self.selectedPiece.getBack().shape[0]):
                    for j in range(self.selectedPiece.getBack().shape[1]):
                        #Check for partial
                        if(self.backArray[x+i][5-(y+j)] != 1)&(self.selectedPiece.getBack()[i][j] != 0):
                            self.backPieces[x+i][5-(y+j)].setColor(self.selectedPiece.getColor())
                            self.backArray[x+i][5-(y+j)] = self.selectedPiece.getBack()[i][j]
                            
            #Back
            else:
                #Check if piece placement is legal
                try:
                    for i in range(self.selectedPiece.getFront().shape[0]):
                        for j in range(self.selectedPiece.getFront().shape[1]):
                            #If the front or back are filled
                            if (self.backArray[x+i][y+j] == 1)&(self.selectedPiece.getFront()[i][j] != 0):
                                print "Wrong Move2.1"
                                print self.backArray
                                return
                            #If the hole is partially filled when placing a piece that goes through
                            elif ((self.backArray[x+i][y+j] == 2)&(self.selectedPiece.getBack()[i][j] == 1)):
                                print "Wrong Move2.2"
                                return
     
                            self.backArray[x+i][y+j]
                            self.frontArray[x+i][5-(y+j)]
                except:
                    print "Wrong Move2.3"
                    return

                for i in range(self.selectedPiece.getFront().shape[0]):
                    for j in range(self.selectedPiece.getFront().shape[1]):
                        if (self.selectedPiece.getFront()[i][j] == 1):
                            self.backPieces[x+i][y+j].setColor(self.selectedPiece.getColor())
                            self.backArray[x+i][y+j] = self.selectedPiece.getFront()[i][j]
                            
                for i in range(self.selectedPiece.getBack().shape[0]):
                    for j in range(self.selectedPiece.getBack().shape[1]):
                        #Check for partial
                        if(self.frontArray[x+i][5-(y+j)] != 1)&(self.selectedPiece.getBack()[i][j] != 0):
                            self.frontPieces[x+i][5-(y+j)].setColor(self.selectedPiece.getColor())
                            self.frontArray[x+i][5-(y+j)] = self.selectedPiece.getBack()[i][j]           

        self.selectedPiece.setInHome(False)
        self.updateGUI()
       
    """Function to take care of mouse clicks."""
    def callback(self,event):
        """What to do if a click occurs"""
        if (event.widget!=self.pieces):
            for i in range(5):
                for j in range(6):
                    if(((event.x > (10+100*j))&(event.x < (90+100*j)))&
                       ((event.y > (10+100*i))&(event.y < (90+100*i)))):
                       
                        self.placePiece(event,i,j)
                        
        else:
            self.select(event.x,event.y)
        return True

    """Function to update the GUI based on the 2D array of size [[1]] pieces and the 
        2D array of fullness."""
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

    """Function to rotate piece. Good call on the rot90 function."""
    def rotatePiece(self):
        self.selectedPiece.rotate()
        self.select(self.selectX,self.selectY)
        self.updateGUI()

"""The piece class. Holds front and back shape, fullness, color, inHome,
    and home coordinates in the top box."""
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
   
"""Calls TK to create the app for the GUI.""" 
def main():
    
    root = Tk()
    app = b2bGUI(master=root)
    app.mainloop()
    root.destroy()

main()
