# https://quera.org/problemset/244100
string = input()

for str in range(int(len(string)/3)):
    findIndex= string.find(".NET")
    if findIndex<0:
        break
    second = string[findIndex+4:]
    first =string[:findIndex]
    newString = first+"Golang"+second
    string = newString


print(string)