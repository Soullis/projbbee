import math

base = 50
sp = 1

class Drone():
    def __init__(self, inX, inY, inZ, inRot = 0):
        self.pos = [inX, inZ, inY]
        self.rot = inRot
        self.m = [50, 50, 50, 50] # FL FR BL BR
        self.lidar_val = self.pos[1]
        self.obj_detector_range = [self.pos[1], self.pos[1] + 10]

    def mma(self, roll, pitch, yaw, throttle):
        if self.pos[1] >= 1:
            self.m[0] += throttle - pitch + roll + yaw 
            self.m[1] += throttle - pitch - roll - yaw 
            self.m[2] += throttle + pitch + roll - yaw 
            self.m[3] += throttle + pitch - roll + yaw 

        self.controls = {"r" : roll, "p" : pitch, "y" : yaw, "t": throttle}
        
        self.pos[0] += self.controls["p"] * sp * math.cos(math.radians(self.rot)) - self.controls["r"] * sp * math.sin(math.radians(self.rot))
        self.pos[2] += self.controls["p"] * sp * math.sin(math.radians(self.rot)) - self.controls["r"] * sp * math.cos(math.radians(self.rot))
        

        if self.pos[1] < 0:
            self.pos[1] = 0
        else:
            self.pos[1] += self.controls["t"] * sp
        self.rot += self.controls["y"] * sp
        self.rot = self.rot % 360

        self.obj_detector_range = [self.pos[2], self.pos[2] + 10]
    
    def command(self, cmmd):
        
        if cmmd == 'rf':
            self.mma(sp, 0, 0, 0)
        if cmmd == 'pf':
            self.mma(0, sp, 0, 0)
        if cmmd == 'yf':
            self.mma(0, 0, sp, 0)
        if cmmd == 'tf':
            self.mma(0, 0, 0, sp)
        if cmmd == 'rb':
            self.mma(-sp, 0, 0, 0)
        if cmmd == 'pb':
            self.mma(0, -sp, 0, 0)
        if cmmd == 'yb':
            self.mma(0, 0, -sp, 0)
        if cmmd == 'tb':
            self.mma(0, 0, 0, -sp)

        for s in self.m:
            if s > 1:
                s = 1

    def lidar(self, alt):
        return self.pos[1] - alt


        
