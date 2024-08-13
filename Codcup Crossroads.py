# https://quera.org/problemset/245888

listShow= []

def getdata(senario):
    global listShow
    for num in  range(senario):
        numebers = input().split(" ")
        n = int(numebers[0])
        m = int(numebers[1])
        handeldata(n,m)
def handeldata(n , m):
    if n>m:
        timer = (n-1)*2
        timer = timer +2
        timer = timer/2
        listShow.append(timer)
               
    if n<m:
        timer = (m-1)*2
        timer = timer +2
        timer = timer/2
        listShow.append(timer)
       
    if n==m:
        timer = (m-1)*2
        timer = timer +2
        timer = timer/2
        timer = timer +1
        listShow.append(timer)
    

senario= int(input())
getdata(senario)

for time in listShow:
    print(int(time))