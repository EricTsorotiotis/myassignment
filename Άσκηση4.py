arithmos = int(input())
lista = list(map(int, (str(arithmos))))
length = len(lista)
if length > 4:
    lista = lista[:4]
tolatin = ""
if length == 1:
    if lista[0] == 1:
        tolatin = tolatin+"I"
    if lista[0] == 2:
        tolatin = tolatin+"II"
    if lista[0] == 3:
        tolatin = tolatin+"III"
    if lista[0] == 4:
        tolatin = tolatin+"IV"
    if lista[0] == 5:
        tolatin = tolatin+"V"
    if lista[0] == 6:
        tolatin = tolatin+"VI"
    if lista[0] == 7:
        tolatin = tolatin+"VII"
    if lista[0] == 8:
        tolatin = tolatin+"VIII"
    if lista[0] == 9:
        tolatin = tolatin+"IX"
if length == 2:
    if lista[0] == 1:
        tolatin = tolatin+"X"
    if lista[0] == 2:
        tolatin = tolatin+"XX"
    if lista[0] == 3:
        tolatin = tolatin+"XXX"
    if lista[0] == 4:
        tolatin = tolatin+"XL"
    if lista[0] == 5:
        tolatin = tolatin+"L"
    if lista[0] == 6:
        tolatin = tolatin+"LX"
    if lista[0] == 7:
        tolatin = tolatin+"LXX"
    if lista[0] == 8:
        tolatin = tolatin+"LXXX"
    if lista[0] == 9:
        tolatin = tolatin+"XC"
    if lista[1] == 1:
        tolatin = tolatin+"I"
    if lista[1] == 2:
        tolatin = tolatin+"II"
    if lista[1] == 3:
        tolatin = tolatin+"III"
    if lista[1] == 4:
        tolatin = tolatin+"IV"
    if lista[1] == 5:
        tolatin = tolatin+"V"
    if lista[1] == 6:
        tolatin = tolatin+"VI"
    if lista[1] == 7:
        tolatin = tolatin+"VII"
    if lista[1] == 8:
        tolatin = tolatin+"VIII"
    if lista[1] == 9:
        tolatin = tolatin+"IX"
if length == 3:
    if lista[0] == 1:
        tolatin = tolatin+"C"
    if lista[0] == 2:
        tolatin = tolatin+"CC"
    if lista[0] == 3:
        tolatin = tolatin+"CCC"
    if lista[0] == 4:
        tolatin = tolatin+"CD"
    if lista[0] == 5:
        tolatin = tolatin+"D"
    if lista[0] == 6:
        tolatin = tolatin+"DC"
    if lista[0] == 7:
        tolatin = tolatin+"DCC"
    if lista[0] == 8:
        tolatin = tolatin+"DCCC"
    if lista[0] == 9:
        tolatin = tolatin+"CM"
    if lista[1] == 1:
        tolatin = tolatin+"X"
    if lista[1] == 2:
        tolatin = tolatin+"XX"
    if lista[1] == 3:
        tolatin = tolatin+"XXX"
    if lista[1] == 4:
        tolatin = tolatin+"XL"
    if lista[1] == 5:
        tolatin = tolatin+"L"
    if lista[1] == 6:
        tolatin = tolatin+"LX"
    if lista[1] == 7:
        tolatin = tolatin+"LXX"
    if lista[1] == 8:
        tolatin = tolatin+"LXXX"
    if lista[1] == 9:
        tolatin = tolatin+"XC"
    if lista[2] == 1:
        tolatin = tolatin+"I"
    if lista[2] == 2:
        tolatin = tolatin+"II"
    if lista[2] == 3:
        tolatin = tolatin+"III"
    if lista[2] == 4:
        tolatin = tolatin+"IV"
    if lista[2] == 5:
        tolatin = tolatin+"V"
    if lista[2] == 6:
        tolatin = tolatin+"VI"
    if lista[2] == 7:
        tolatin = tolatin+"VII"
    if lista[2] == 8:
        tolatin = tolatin+"VIII"
    if lista[2] == 9:
        tolatin = tolatin+"IX"
if arithmos == 1000:
    tolatin = "M"
print("The number that you entered in latin:", tolatin)
