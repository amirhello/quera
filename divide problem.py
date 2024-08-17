number = int(input())

counter=0
sumation = 0

for i in range(1,number+1):
    for x in range(1,i+1):
        if i%x == 0:
            counter = counter+1
            sumation = sumation+x


print(counter,sumation)


