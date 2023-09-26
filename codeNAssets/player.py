class player:

    x = 499
    y = 499
    stamina = 100
    minSpeed = 240 #pixels per second
    acceleration = 92 #pixels per second squared
    maxSpeed =  600 #pixels per second

    def __init__(self, name, seed):
        self.name = name
        self.seed = seed