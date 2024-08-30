# https://quera.org/problemset/218362


num = input()
num = input().split()
num2 = input()

val1 = False
val2= False

if "1" in num :
    val1 = True

if "0" in num: 
    val2=True

if val2 and val1:
    print("YES")
else:
    print("NO")
