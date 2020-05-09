from math import *
import random
import copy

global a
global b
a=[0,2,4]
b=[2,4]

def init():
    table_x=[]
    table=[]
    for j in range (0,4):
        for i in range(0,4):
            x=random.choice(a)
            table_x.append(x)
        table.append(table_x)
        table_x=[]
    return(table)
        
def droite(table):
    for x in range(4):
        for i in range(0,4):
            for j in reversed(range(1,4)):
                if table[i][j]==0:
                    table[i][j]=table[i][j-1]
                    table[i][j-1]=0
    for i in range(0,4):
        init_range=4
        for j in reversed(range(1,init_range)):
            if table[i][j]==table[i][j-1]:
                init_range=j
                table[i][j]=table[i][j-1]*2
                table[i][j-1]=0
    for x in range(4):
        for i in range(0,4):
            for j in reversed(range(1,4)):
                if table[i][j]==0:
                    table[i][j]=table[i][j-1]
                    table[i][j-1]=0
    return(table)

def gauche(table):
    for x in range(4):
        for i in range(0,4):
            for j in range(0,3):
                if table[i][j]==0:
                    table[i][j]=table[i][j+1]
                    table[i][j+1]=0
    for i in range(0,4):
        init_range=0
        for j in range(init_range,3):
            if table[i][j]==table[i][j+1]:
                init_range=j+1
                table[i][j]=table[i][j+1]*2
                table[i][j+1]=0
    for x in range(4):
        for i in range(0,4):
            for j in range(0,3):
                if table[i][j]==0:
                    table[i][j]=table[i][j+1]
                    table[i][j+1]=0
    return(table)

def haut(table):
    init_range=0
    for k in range(4):
        for x in range(4):
            for i in range(0,3):
                for j in range(0,4):
                    if table[i][j]==0:
                        table[i][j]=table[i+1][j]
                        table[i+1][j]=0                       
        for x in range(4):
            for i in range(init_range,3):
                for j in range(0,4):
                    if table[i][j]==table[i+1][j]:
                        init_range=i+1
                        table[i][j]=table[i+1][j]*2
                        table[i+1][j]=0
    return(table)

def bas(table):
    init_range=4
    for k in range(4):
        for x in range(4):
            for i in reversed(range(1,4)):
                for j in range(0,4):
                    if table[i][j]==0:
                        table[i][j]=table[i-1][j]
                        table[i-1][j]=0                       
        for x in range(4):
            for i in reversed(range(1,init_range)):
                for j in range(0,4):
                    if table[i][j]==table[i-1][j]:
                        init_range=i
                        table[i][j]=table[i-1][j]*2
                        table[i-1][j]=0
    return(table)

def scan(table,k):
    coord=[]
    for i in range(4):
        for j in range(4):
            if table[i][j]==k:
                coord.append([i,j])
    return(coord)

def random_generate(table):
    coord=scan(table,0)
    i=random.choice(coord)
    nbr=random.choice(b)
    table[i[0]][i[1]]=2
    return(table)

def compare_list(list1,list2):
    for i in range(4):
        for j in range(4):
            if list1[i][j]!=list2[i][j]:
                return False
    return True

def perdu(table):
    temp=copy.deepcopy(table)
    scan0=scan(temp,0)
    table1=droite(temp)
    table1=gauche(temp)
    table1=haut(temp)
    table1=bas(temp)
    scan1=compare_list(temp,table1)
    if scan1:
        if len(scan0)==0:
            return "perdu"
    return "non_perdu"

def afficher(table):
    maximum=0
    for i in table:
        maximum=max(maximum,max(i))
    maximum=len(str(maximum))
    for i in table:
        for j in i:
            print(j,' '*(maximum-len(str(j))),end="")
        print()

def jouer():
    play=init()
    perd=""
    afficher(play)
    while perd!="perdu":
        dep=input("Choisissez un déplacement:")
        if dep=="droite":
            play=droite(play)
        elif dep=="gauche":
            play=gauche(play)
        elif dep=="haut":
            play=haut(play)
        elif dep=="bas":
            play=bas(play)
        else:
            continue
        perd=perdu(play)
        if perd!="perdu":
            play=random_generate(play)
            afficher(play)
        else:
            afficher(play)
            print("perdu")
            
jouer()
