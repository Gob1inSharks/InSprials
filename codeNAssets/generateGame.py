import random
import math


"""

"""
def generateMap(seedNum,filename):
    random.seed(a = seedNum)
    orgRandomState = random.getstate()
    #print("Seed: " + str(random.getstate()))
    #filename = filename + '.txt'
    #fout = open(filename, 'w') #save map to file for saving game or debugging

    map = [[0 for i in range(10**3)] for j in range(10**3)]

    INTERSECTIONS_NUM = 10**4
    STALK_CHANCE = 33 #percent
    RAGE_CHANCE = 10 #percent
    ITEM_CHANCE = 50 #percent

    intersections = [(random.randint(1,10**3-1),random.randint(1,10**3-1)) for i in range(INTERSECTIONS_NUM)]
    for xy in intersections:
        if random.randint(1,100) <= ITEM_CHANCE:
            map[xy[0]][xy[1]] = 4
        else:
            if random.randint(1,100) <= STALK_CHANCE:
                map[xy[0]][xy[1]] = 6
            else:    
                map[xy[0]][xy[1]] = 5

    map[499][499] = '1'

    """
    for i in range(10**3):
        for j in range(10**3):
            fout.write(str(map[i][j])+' ')
        fout.write('\n')
    """

    gameName = filename

    return map, gameName

if __name__ == '__main__':
    generateMap(500,'map')