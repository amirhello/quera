# https://quera.org/problemset/236459?tab=description




timer =int(input())
numberOfAparteman= int(input())
hightOfaparteman=input().split(" ")

# print(hightOfaparteman)
sum = 0
time = 0

hight= 0 
counter = 0
for  hi in hightOfaparteman:
    time = time+1

    hi =int(hi)
    if counter ==len(hightOfaparteman)-1:
        time = time + int(hi/timer)
        if  hi%timer>0:
            time = time + 1
    if counter==0:
        hight  = hi
        sum = hight
        time= int(sum/timer)+time
        if  sum%timer>0:
            time = time + 1
        counter =counter+1
        # time = time+1
        continue
    if hi>hight:
        sum = (hi-hight)
        # time= time+1 + int(sum/timer)
        time= time+ int(sum/timer)
        if  sum%timer>0:
            time = time + 1
        hight = hi
        counter =counter+1
        continue
    if  hi==hight:
        # time = time+1
        counter =counter+1
    if  hi<hight:
        sum = ( hight -hi )
        # time = time + 1 + int(sum/timer)
        time = time + int(sum/timer)
        if  sum%timer>0:
            time = time + 1
        hight =hi
        counter =counter+1
        continue
    
    

# for num in range(numberOfAparteman):
#     if num==numberOfAparteman-1:
#           sum = int(hightOfaparteman[num])+sum
#           time= time+1
#           break

#     if num ==0 :
#           sum = int(hightOfaparteman[num])+sum
#           time = time+1 
#           continue
#     if int(hightOfaparteman[num])<int(hightOfaparteman[num+1]):
#             sum=int(hightOfaparteman[num]) +sum
#             time = time+1 

#     if int(hightOfaparteman[num])==int(hightOfaparteman[num+1]):
#           time = time+2

#     if int(hightOfaparteman[num])>int(hightOfaparteman[num+1]):
#           sum = int(hightOfaparteman[num])+sum + (int(hightOfaparteman[num])-int(hightOfaparteman[num+1])) 
#           time = time+2


print(time)
