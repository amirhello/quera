
listprint =[]


def getinput():
    senario = input()
    global listprint
    for item in range(int(senario)):
        color  =input()
        red =color[1:3]
        green =color[3:5]
        blue =color[5:]
        numberRed =hexToDesimal(red)
        numberBlue =hexToDesimal(blue)
        numberGreen =hexToDesimal(green)
        completRed =255-numberRed
        completGreen =255 -numberGreen
        completBlue =255-numberBlue
        hexRed = desimalToHex(completRed)
        hexGreen = desimalToHex(completGreen)
        hexBlue = desimalToHex(completBlue)

        listprint.append(f"#{hexRed}{hexGreen}{hexBlue}")

def hexToDesimal(color):
    numberRight=0
    numberLeft=0
    if color[0]=="F":
        numberRight= 15*16
    elif color[0]=="E":
        numberRight= 14*16
    elif color[0]=="D":
        numberRight= 13*16
    elif color[0]=="C":
        numberRight= 12*16
    elif color[0]=="B":
        numberRight= 11*16
    elif color[0]=="A":
        numberRight= 10*16
    else:
        numberRight = int(color[0])*16
        # -----------------------------------
    if color[1]=="F":
        numberLeft= 15
    elif color[1]=="E":
        numberLeft= 14
    elif color[1]=="D":
        numberLeft= 13
    elif color[1]=="C":
        numberLeft= 12
    elif color[1]=="B":
        numberLeft= 11
    elif color[1]=="A":
        numberLeft= 10
    else:
        numberLeft = int(color[1])

    return numberRight+numberLeft
    

def desimalToHex(color):
    submultiple = int(color/16)
    remainder =color%16
    rightHex= ""
    leftHex = ""
    if submultiple==15:
        rightHex ="F"
    elif submultiple==14:
        rightHex ="E"
    elif submultiple==13:
        rightHex ="D"
    elif submultiple==12:
        rightHex ="C"
    elif submultiple==11:
        rightHex ="B"
    elif submultiple==10:
        rightHex ="A"
    else:
        rightHex=f"{submultiple}"
        # -------------------------------
    if remainder==15:
        leftHex ="F"
    elif remainder==14:
        leftHex ="E"
    elif remainder==13:
        leftHex ="D"
    elif remainder==12:
        leftHex ="C"
    elif remainder==11:
        leftHex ="B"
    elif remainder==10:
        leftHex ="A"
    else:
        leftHex=f"{remainder}"
    return rightHex+leftHex



    pass



getinput()


for part in listprint:
    print(part)