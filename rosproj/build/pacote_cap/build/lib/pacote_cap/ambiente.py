from drone import Drone

drone = Drone(500, 0, 0, 90)

arena = [1000, 1000]
fX = 500
fY= 200
fSize = 100
fH = 100

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

            8 = face frontal base
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
        if id == 8:
            return [self.posX, self.posX + self.size]
    

obstaculos = [Obstaculo(fSize, fX, fY, fH), Obstaculo(fSize, fX + 100, fY, fH), Obstaculo(fSize, fX - 100, fY, fH)]
current_obs = 0

        

