import pygame as pg
import random
import drone

d = drone.Drone(400, 300, 0)


pg.init()

class DronePlayer(pg.sprite.Sprite):
    def __init__(self, image_name, pos_x, pos_y):
        super().__init__()
        self.orig_imag = pg.image.load(image_name).convert_alpha()
        self.image = self.orig_imag.copy()
        self.rect = self.image.get_rect()
        self.rect.center = (pos_x, pos_y)

        self.mask = pg.mask.from_surface(self.image)
        self.old_rect = self.rect.copy()

    def rotate(self):
        self.image = pg.transform.rotate(self.orig_imag, d.rot)
        old_center = self.rect.center
        self.rect = self.image.get_rect(center=old_center)
        self.mask = pg.mask.from_surface(self.image)

    def update(self, keys):
        if keys[pg.K_UP]:
            d.command('tf')
        if keys[pg.K_DOWN]:
            d.command('tb')
        if keys[pg.K_LEFT]:
            d.command('yf')
        if keys[pg.K_RIGHT]:
            d.command('yb')
        if keys[pg.K_w]:
            d.command('rf')
        if keys[pg.K_s]:
            d.command('rb')
        if keys[pg.K_a]:
            d.command('pb')
        if keys[pg.K_d]:
            d.command('pf')
            
        drone.rect.y = d.pos[2]
        drone.rect.x = d.pos[0]
        self.rotate()
        
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > screen_width:
            self.rect.right = screen_width
        if self.rect.top < 0:
            self.rect.top = 0
        if self.rect.bottom > screen_height:
            self.rect.bottom = screen_height
        
        
class Slalon(pg.sprite.Sprite):
    
    def __init__(self, pos_x, pos_y, r):
        super().__init__()
        self.image = pg.Surface([r * 2, r * 2], pg.SRCALPHA)
        self.alt = random.randint(25, 200)
        
        pg.draw.circle(self.image, (0, 0, 0), (r, r), r)
        
        self.rect = self.image.get_rect()
        self.rect.center = (pos_x, pos_y)

        font_size = int(r * 1.2)
        font = pg.font.Font(None, font_size)
        text_surface = font.render(str(self.alt), True, (255, 255, 255))
        text_rect = text_surface.get_rect(center=(r, r))
        self.image.blit(text_surface, text_rect)
        


screen_width = 800
screen_height = 600
screen = pg.display.set_mode((screen_width, screen_height))
pg.display.set_caption("Drone Simulation")
font = pg.font.Font(None, 36)

drone = DronePlayer('drone.png', d.pos[0], d.pos[2])
slalons = pg.sprite.Group()

all_sprites = pg.sprite.Group()
all_sprites.add(drone)


for _ in range(10): 
    obs_x = random.randint(0, screen_width)
    obs_y = random.randint(0, screen_height) + 80
    obs_radius = random.randint(10, 30)

    obstacle = Slalon(obs_x, obs_y, obs_radius)
    
    slalons.add(obstacle)
    all_sprites.add(obstacle)

running = True
clock = pg.time.Clock()
while running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False

    key_pressed = pg.key.get_pressed()
    all_sprites.update(key_pressed)
    

    collided_obstacles = pg.sprite.spritecollide(drone, slalons, False, pg.sprite.collide_mask)
    if collided_obstacles:
        for o in collided_obstacles:
            if d.lidar(o.alt) < 0:
                drone.rect.topleft = drone.old_rect.topleft
                d.pos[2] = drone.rect.y
                d.pos[0] = drone.rect.x
            d.lidar_val = d.lidar(o.alt)
    else:
        d.lidar_val = d.lidar(0)


    if d.pos[1] > 0:
        screen.fill((135, 206, 235))
    else:
        screen.fill((255, 255, 255))
        
    all_sprites.draw(screen)

    pos_text = f"FL: {d.m[0]:.2f} FR: {d.m[1]:.2f} BL: {d.m[2]:.2f} BR: {d.m[3]:.2f} Lidar {d.lidar_val:.2f} R {d.rot:.2f}"
    text_surface = font.render(pos_text, True, (0, 0, 0)) 
    screen.blit(text_surface, (10, 10))

    print(drone.rect.x, " ", drone.rect.y)

    pg.display.flip()
    clock.tick(60)

pg.quit()