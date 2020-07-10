# Def des import -->
import random

# def des fonction -->
def printMap(positionTrain, map):
    map[positionTrain] = "T"
    return map


# def de variable -->
Energy = int(input("initial energy? : "))
longWay = int(input("longueur de la voie entre 50 et 100"))
container = [" "] * longWay
trainway = []
service_station = [" "] * longWay
pick_up = True
maxEnergy = int(input("energie max"))
maxCharge = int(input("charge max"))
statutParty = "ok"
map = ["-"] * longWay
train_position = 0
consumption = 1
bloc_energie=int(input("Combien de bloc d'energie ? : "))
bloc_energie_max=int(input("Combien d'energie il y a au max dans un bloc"))
how_much_for_pickup = int(input("how_much_energy_for_pickup? :"))

for i in range(len(bloc_energie)):
    service_station.append(random.randint(1,10))



# def du main -->

# condition de fin de jeu

while Energy > 0:
    continue
    if maxEnergy == 0:
        print("c'est perdu le train est en panne")
    break
    print(printMap(train_position, map))

while 50 >= longWay > 100
    longWay = int(input("longueur de la voie entre 50 et 100"))