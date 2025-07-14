arena = [1000, 1000]

class Obstaculo():
    def __init__(self, size, posX, posY, alt):
        self.size = size
        self.posX = posX
        self.posY = posY
        self.alt = alt

    def limits(self, id):
        """
        
            7 +----+ 6
             /    /|
          4 +----+ | 5
            |  3 | + 2
            |    |/
            +----+
            0    1
        """
        if id == 0:
            return [self.posX, self.posY, 0]
        if id == 1:
            return [self.posX + self.size, self.posY, 0]
        if id == 2:
            return [self.posX + self.size, self.posY + self.size, 0]
        if id == 3:
            return [self.posX, self.posY + self.size, 0]
        if id == 4:
            return [self.posX, self.posY, self.alt]
        if id == 5:
            return [self.posX + self.size, self.posY, self.alt]
        if id == 6:
            return [self.posX + self.size, self.posY + self.size, self.alt]
        if id == 7:
             return [self.posX, self.posY + self.size, self.alt]
    

obstaculos = [Obstaculo(500, 200, 100), Obstaculo(600, 400, 100), Obstaculo(400, 600, 100)]


        

