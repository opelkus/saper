import random

rozmiar=[9,16]


procent=20





def miner():
    global stan
    global lista
    global rozmiar
    stan=[]
    lista=[True]*procent+[False]*(rozmiar[0]*rozmiar[1]-procent)
    for i in range(rozmiar[0]):
        rzad=[]
        for y in range(rozmiar[1]):
            czy_bomba=lista[random.randint(0,(len(lista)-1))]
            lista.remove(czy_bomba)
            if czy_bomba:
                rzad.append([10,False,0])
            else:
                rzad.append([0,False,0])
        stan.append(rzad) 
        


def around(x,y,ktora=10):
    global stan
    global rozmiar
    out=[]
    if x > 0:
        rzad=stan[x-1]
        out.append(rzad[y])
        if y > 0:
             out.append(rzad[y-1])
        if y <(rozmiar[1]-1):
                    out.append(rzad[y+1])
    
    if x < (rozmiar[0]-1):
        rzad=stan[x+1]
        out.append(rzad[y])
        if y > 0:
             out.append(rzad[y-1])
        if y <(rozmiar[1]-1):
                    out.append(rzad[y+1])

    rzad=stan[x]
    
    if y > 0:
             out.append(rzad[y-1])
    if y <(rozmiar[1]-1):
                    out.append(rzad[y+1])
    if ktora<10:
        aray=[]
        for i in out:
            aray.append(i[ktora])
            
        out=aray
    return(out)


def geolog():
    global stan
    global rozmiar
    for x in range(rozmiar[0]):
        for y in range(rozmiar[1]):
            
            pole=10==stan[x][y][0]
            pola=around(x,y,0)
            if pole and pola.count(10) ==8:
                stan[x][y][0]=8
            
            if not pole:
               stan[x][y][0]=int(pola.count(10))
        




miner()
print("\n\n\n\n")
geolog()
