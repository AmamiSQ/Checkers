class Player:
    """ Player class """

    #attributes
    score = 0
    color = None
    stones = None
    turn = False

    def __init__(self, color):
        self.color = color
        self.stones = []
        self.turn = False

    def addStone(self, stone):
        self.stones.append(stone)

    def removeStone(self, stone):
        self.stones.remove(stone)
    
    def getStones(self):
        return self.stones
    
    def getScore(self):
        return self.score
    
    def setScore(self, score):
        self.score = score

    def getColor(self):
        return self.color
    
    def setColor(self, color):
        self.color = color

    def getTurn(self):
        return self.turn
    
    def setTurn(self, turn):
        self.turn = turn

