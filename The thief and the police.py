# https://quera.org/problemset/244102


police= int(input())
robber = int(input())

moveCounter= 0

sampleSpace=[
    [1,1,1,1,0,0,0]
    ,[1,1,1,1,1,1,0]
    ,[1,1,1,1,0,1,1]
    ,[1,1,1,1,1,1,1]
    ,[0,1,0,1,1,1,0]
    ,[0,1,1,1,1,1,1]
    ,[0,0,1,1,0,1,1]
]




def print_matrix(m):
    for row in m:
        for coulmn in row:
            print(coulmn , end=" ")
        print()


def finded():
    if police==robber:
        print(moveCounter)


def Onemove():
    global police
    global moveCounter
    if sampleSpace[robber-1][police-1]==1 or sampleSpace[police-1][robber-1]==1 :
        moveCounter = moveCounter +1
        print(moveCounter)
    else:
        police = 4 
        moveCounter = 1
        Onemove()

        


# print_matrix(sampleSpace)


finded()
Onemove()


