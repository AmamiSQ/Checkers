class Stone:
    """A class to define the stones used in Checkers."""
    
    #attributes
    color = None
    king = False
    position = None


    def __init__(self, color):
        self.color = color
        self.king = False
        self.position = None
    
    
    

