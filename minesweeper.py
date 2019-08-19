import random as r
import copy

class minesweeper:
    def __init__(self,len,lvl):
        self.backmatrix=list()
        self.frontmatrix=list()
        self.len=len
        self.lvl=lvl
        self.empty=list()

    def genEmptyMatrix(self):
        for i in range(self.len):
            self.backmatrix.append(list())
            for j in range(self.len):
                self.backmatrix[i].append("-") 

    def checkField(self,field):
        if self.backmatrix[field[0]][field[1]]==".":
            print("end game")
        else:
            if isinstance(self.backmatrix[field[0]][field[1]],int): 
                self.frontmatrix[field[0]][field[1]]=self.backmatrix[field[0]][field[1]]
            else:        
                self.frontmatrix[field[0]][field[1]]=str()
            self.clearNeighboringFields(field)
    
    def clearNeighboringFields(self,field):
        for i in [[-1,-1],[-1,0],[-1,1],[0,-1],[0,1],[1,-1],[1,0],[1,1]]:
            X=field[0]+i[0] 
            Y=field[1]+i[1]
            if X>=0 and Y>=0 and X<=self.len-1 and Y<=self.len-1 and [X,Y] not in self.empty:
                if self.backmatrix[X][Y]=="-":
                    self.frontmatrix[X][Y]=str()
                    self.empty.append([X,Y])                   
                    self.clearNeighboringFields([X,Y])
                if self.backmatrix[X][Y] in list(range(10)):
                    print([X,Y])
                    if isinstance(self.backmatrix[X][Y], int): 
                        self.frontmatrix[X][Y]=self.backmatrix[X][Y]
                   
                    

            else:
                pass

    def incrementMinesNeighboring(self,field):
        for i in [[-1,-1],[-1,0],[-1,1],[0,-1],[0,1],[1,-1],[1,0],[1,1]]:
            X=field[0]+i[0] 
            Y=field[1]+i[1]
            if X>=0 and Y>=0 and X<=self.len-1 and Y<=self.len-1:
                if self.backmatrix[X][Y]=="-":
                   self.backmatrix[X][Y]=1
                else:
                   if  isinstance(self.backmatrix[X][Y],int):
                        print(self.backmatrix[X][Y])
                        self.backmatrix[X][Y]=self.backmatrix[X][Y]+1

    def setupMines(self):
        try:
            choisedList=list()
            self.backmatrix.clear()
            self.genEmptyMatrix()
            self.frontmatrix=copy.deepcopy(self.backmatrix)
            
            i=0
            while i <= int(len(self.backmatrix)*len(self.backmatrix[0])*self.lvl): 
                choiced=[int(r.choice(range(int(len(self.backmatrix))))),int(r.choice(range(int(len(self.backmatrix[0])))))]
                print(choiced)
                if choiced not in choisedList:
                    i+=1
                    choisedList.append(choiced)
                    self.backmatrix[choiced[0]][choiced[1]]="."
                    self.incrementMinesNeighboring([choiced[0],choiced[1]])
                    
                
          #  for i in range(int(len(self.backmatrix)*len(self.backmatrix[0])*self.lvl)):
          #      choiced=[int(r.choice(range(int(len(self.backmatrix))))),int(r.choice(range(int(len(self.backmatrix[0])))))]
          #      print(choiced)
          #      self.backmatrix[choiced[0]][choiced[1]]=True
          #      self.incrementMinesNeighboring([choiced[0],choiced[1]])
          #      choisedList.append(choiced)
            
            
           # check=[]
           # for i in choisedList:
           #     if i not in check:
           #         check.append(i)
            
           # if len(choisedList)!=len(check):
           #     print("next round")
           #     choisedList.clear()
           #     self.setupMines() 
        except Exception:
            print("try again please")