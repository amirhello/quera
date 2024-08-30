# https://quera.org/problemset/168945



matrix = []

arrey1 = list(input())
arrey2 = list(input())
arrey3 = list(input())
matrix.append(arrey1)
matrix.append(arrey2)
matrix.append(arrey3)


counterX= 0
counterO= 0
for rows in matrix :
    for columns in rows :
        if columns=="X":
            counterX= counterX +1
        if columns=="O":
            counterO = counterO +1

if counterO>counterX:
    print("Invalid")
    exit()

if counterX>counterO+1:
    print("Invalid")
    exit()
        



def findDiameter(row,column ,value):
    # if row==0 and column==0 :
        if matrix[0][0]==value:
            if matrix[1][1]==value:
                if matrix[2][2]==value:
                    return True
    # if row==2 and column==0 :
        if matrix[0][2]==value:
            if matrix[1][1]==value:
                if matrix[2][0]==value:
                    return True
def findRow(row ,column,value):
    if row == 0 :
        if matrix[row][column]==value:
            if matrix[row+1][column]==value:
                if matrix[row+2][column]==value:
                    return True

def findColumn(row ,column,value):
    if column == 0 :
        if matrix[row][column]==value:
            if matrix[row][column+1]==value:
                if matrix[row][column+2]==value:
                    return True

def calculate():
    winer= set()
    counterQ= 0
    for row in range(3):
        for column in range(3):
            value = matrix[row][column]
            if  value =="X":
                rowValue=findRow(row ,column , value)
                columnValue=findColumn(row ,column , value)
                diameterValue = findDiameter(row ,column , value)
                if rowValue or columnValue or diameterValue :
                    winer.add("X")
                    
            if  value =="O":
                rowValue=findRow(row ,column , value)
                columnValue=findColumn(row ,column , value)
                diameterValue = findDiameter(row ,column , value)
                if rowValue or columnValue or diameterValue :
                    winer.add("O")
            if value=="?":
                counterQ =counterQ+1



    if len(winer)>1:
        print("Invalid")
        exit()
    if len(winer)==1:
        print(winer.pop())
        exit()
    if counterQ>0:
        print("Unfinished")
        exit()
    else:
        print("Draw")



calculate()



'''

OXO
XOX
OOO

XOX
XOX
OXO

XXO
OXO
XOO

XXO
XOO
XXO

OXO
XXO
OXX

OXO
XXX
XOX

OXX
OXX
?XO

OXX
OXX
?OX

XOX
OXO
??X


XOX
XOX
XOO


XOX
OXX
OXO

XOX
OXO
XOX

XXX
XXO
OOO

OOO
OOO
OOO

OXO
XOX
XOX

XOX
OX?
XO?
# problem



'''