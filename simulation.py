import drone
import visualization as vz
import time

d = drone.Drone()

isRunning = False

while isRunning:
    cmmd, sp = input("Comando: ").split()
    sp = int(sp)
    # Comandos de Movimento

    # if vz.isObstacle(x, y):
    #     d.rot += 1
    # else:
    #     d.pitch(-sp)

    if cmmd == 't':
        d.throttle(sp)
    elif cmmd == 'y':
        d.yaw(sp)
    elif cmmd == 'r':
        d.roll(sp)
    elif cmmd == 'p':
        d.pitch(sp)
    elif cmmd == 'zigzag':
        d.pitch(sp)
        time.sleep(1)
        d.roll(sp)
        time.sleep(1)
        d.pitch(sp)
        time.sleep(1)
        d.roll(-2*sp)
        time.sleep(1)
        
    elif cmmd == 'circle':
        d.pitch(sp)
        d.roll(sp)
        time.sleep(1)
        d.pitch(sp)
        d.roll(-sp)
        time.sleep(1)
        d.pitch(-sp)
        d.roll(-sp)
        time.sleep(1)
        d.pitch(sp)
        d.roll(sp)
        time.sleep(1)

    # Referencia

    elif cmmd == 'pos':
        print(f"{d.pos}")
    elif cmmd == 'rot':
        print(f"{d.rot}")
    elif cmmd == 'a':
        print(f"mFL{d.mFL.a} mFR{d.mFR.a} mBL{d.mBL.a} mBR{d.mBR.a} ")

    # Programa

    elif cmmd == 'q':
        isRunning = False
    else:
        print("Comando nao detectado")

    
