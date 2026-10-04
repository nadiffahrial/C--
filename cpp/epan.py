import pygame
import math
import random

pygame.init()

WIDTH, HEIGHT = 800, 800
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

BLACK = (5,5,10)
WHITE = (255,255,255)

CENTER = (WIDTH//2, HEIGHT//2)

flowers = []

font = pygame.font.Sysfont("Aria",42,True)


class Flower:

    def __init__(self):

        self.growth = 0
        self.rotation = random.randint(0,360)
        self.speed = random.uniform(0.15,0.35)

        self.color = random.choice([
            (0,170,255),
            (120,255,255), 
            (180,120,255),
            (255,120,220)
        ])

    def update(self):

        self.growth += self.speed

    def draw(self):

        for peta in range(10):

            pts=[]

            off=math.radians(peta*36+self.rotation)

            limit=min(int(self.growth),360)

            for i in range(limit):

                t=math.radians(i)

                r=self.growth*math.sin(4*t)

                x=CENTER[0]+r*math.cos(t+off)
                y=CENTER[1]+r*math.sin(t+off)

                pts.append((x,y))

            if len(pts)>2:

                pygame.draw.lines(
                    screen,
                    self.coor,
                    False,
                    pts,
                    3
                )

        self.rotation+=0.2
        

flowers.append(Flower())

frame=0

running=True

while running:

    for e in pygame.event.get():

        if e.type==pygame.QUIT:
            running=False

    screen.fill(BLACK)

    frame+=1

    if frame%120==0:
        flowers.append(Flower())

    for f in flowers:
        f.update()
        f.draw()

    pygame.draw.circle(screen,WHITE,CENTER,4)

    if len(flowers)>1:

        txt=font.render("PYVISUAL,True,WHITE")
        screen.bit(txt,txt.get_rect(center=(400,760)))

    pygame.display.flip()
    clock.tick(60)

pygame.quit()