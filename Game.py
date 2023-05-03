#######Imports###############
import pygame, math, random

#### COLORS ####
orange = (255,171,0)
blue = (0,255,255)
green = (0,255,128)
white = (255,255,255)

########Variables############
H = 1000 #Ширина
W = 800 #Высота
run = True
bullets = []
clock = pygame.time.Clock()
numRays = 101
screen = pygame.display.set_mode((H,W))
tile = 400
scaleX = H // numRays
dist = numRays / (2 * math.tan(math.pi/3))
FOV = math.pi / 3
deltaAngle = FOV / numRays        # FOV / numRays

##########Run################
pygame.init()

###########Classes###########
class Ray:
    def __init__(self, angle):
        self.angle = angle

    def DrawRay(self):
        GHP = self.GetHitPoint()

        pygame.draw.line(screen,"yellow",(player.posX, player.posY), GHP)

        pygame.draw.circle(screen, "green", GHP, 5)

    def GetDepth(self):
        lenX = W * math.cos(self.angle) / 100 #Parts of rayX (1/100) Части лучаХ (поделили его на 100 маленьких частей)  player.posX +
        lenY = W * math.sin(self.angle) / 100 #Parts of rayY (1/100) player.posY +

        for i in range(1,100): # Founding the point by multiplying it on i
            if (len(map.map) > (player.posY + lenY * i )// 100 >= 0 and len(map.map[0]) > (player.posX + lenX * i) // 100 >= 0): # can check next string?
                if (map.map[int((player.posY + lenY * i) // 100)][int((player.posX + lenX * i) // 100)] == 1): # if in block:
                    return (i) # return depth
        return (10000000)
    
    def GetHitPoint(self):
        lenX = W * math.cos(self.angle) / 100 #Parts of rayX (1/100) Части лучаХ (поделили его на 100 маленьких частей)  player.posX +
        lenY = W * math.sin(self.angle) / 100 #Parts of rayY (1/100) player.posY +

        for i in range(1,100): # Founding the point by multiplying it on i
            if (len(map.map) > (player.posY + lenY * i )// 100 >= 0 and len(map.map[0]) > (player.posX + lenX * i) // 100 >= 0): # can check next string?
                if (map.map[int((player.posY + lenY * i) // 100)][int((player.posX + lenX * i) // 100)] == 1): # if in block:
                    return (player.posX + lenX * i, player.posY + lenY* i) # return point
        return (0,0)



class Map:
    def __init__(self):
        self.prevX = 0
        self.prevY = 0

        self.map = [
            [1, 1,  1,  1,  1,  1,    1,    1,  1,  1],
            [1,'pl','_','_','_','_',  '_', '_','_', 1],
            [1,'_','_','_','_','_',   '_', '_','_',1],
            [1,'_','_','_', 1,  1,    '_', '_','_',1],
            [1,'_','_','_', 1,  1,    '_', '_','_',1],
            [1,'_','_','_','_', '_',  '_', 1,'_',1],
            [1,'_' ,'_', '_','_', '_','_', 1,'_',1],
            [1,'_' ,'_', '_','_','_','_', 1,'_',1],
            [1, 1,  1,  1,'_','_', '_',  1,  1, 1],
            [1,'_','_','_','_','_', '_','_','_',1],
            [1,'_','_','_','_','_', '_',  '_','_',1],
            [1,'_', 1,  1, '_',  1,  1,   '_','_',1],
            [1,'_','_','_','_', '_', 1,   '_','_',1],
            [1,'_','_','_',1, '_', '_', '_','_',1],
            [1,'_', 1 ,'_','_','_', '_', 1,  1,1],
            [1,'_','_','_','_','_', '_', '_','_',1],
            [1, 1,  1,  1,  1,  1,  1,  1,  1,  1],
        ]

        self.colorMap = [
            [orange, orange,  orange,  orange,  orange,  orange,  orange,  orange, orange, orange],
            [orange, '_',   '_',      '_',     '_',     '_',     '_',     '_',     '_',    orange],
            [orange, '_',   '_',      '_',     '_',     '_',     '_',     '_',     '_',    orange],
            [orange, '_',   '_',      '_',     orange, orange,    '_',     '_',     '_',    orange],
            [orange, '_',   '_',      '_',     orange, orange,    '_',     '_',     '_',    orange],
            [orange, '_',   '_',      '_',     '_',     '_',     '_',     orange,    '_',    orange],
            [orange, '_' ,  '_',      '_',     '_',     '_',     '_',     orange,    '_',    orange],
            [orange, '_' ,  '_',      '_',     '_',     '_',     '_',     orange,    '_',    orange],
            [orange, orange,orange,  orange,   '_',     '_',     '_',   orange,  orange,    orange],
            [orange, '_',   '_',      '_',     '_',     '_',     '_',     '_',     '_',    orange],
            [orange, '_',   '_',      '_',     '_',     '_',     '_',     '_',     '_',    orange],
            [orange, '_',   orange,   orange,  '_',    orange, orange,     '_',     '_',    orange],
            [orange, '_',   '_',      '_',     '_',     '_',    orange,     '_',     '_',    orange],
            [orange, '_',   '_',      '_',     orange,     '_',     '_',     '_',     '_',    orange],
            [orange, '_',   orange,      '_',     '_',     '_',     '_',     orange,     orange,    orange],
            [orange, '_',   '_',      '_',     '_',     '_',     '_',     '_',     '_',    orange],
            [orange, orange, orange,   orange,  orange,  orange,  orange,  orange,  orange,  orange],
        ]

        self.possibleSelect = []

    def draw(self): # Draw 2D
        for j in range(W // 100):
            for i in range(H // 100):
                if (self.map[j][i] == 1):
                    pygame.draw.rect(screen,'darkgray',(i*100, j*100, 100, 100))

    def newDraw(self): # Draw 3D
        for curRay in range(numRays):
            GHPx,GHPy = rays[curRay].GetHitPoint()
            proj_coff = dist * tile
            depth = rays[curRay].GetDepth() 
            proj_h = proj_coff / depth
            depth *= math.cos(player.angle - rays[curRay].angle)
            c1,c2,c3 = self.colorMap[int(GHPy//100)][int(GHPx//100)]
            if (c1 - depth*3 < 0):
                c1 = 0
            else:
                c1 -= depth * 3
            if (c2 - depth * 3< 0):
                c2 = 0
            else:
                c2 -= depth * 3
            if (c3 - depth * 3< 0):
                c3 = 0
            else:
                c3 -= depth * 3
            pygame.draw.rect(screen, [c1, c2, c3],
                            (scaleX * curRay, W / 2 - proj_h // 2, scaleX, proj_h))
            
        
    def MiniMap(self):
        for j in range(len(map.map)):
            for i in range(len(map.map[0])):
                if (self.map[j][i] == 1):
                    pygame.draw.rect(screen,'darkgray',(i*10, j*10, 10, 10))
        pygame.draw.circle(screen,'green',(player.posX/10, player.posY/10),3)
    
    def NewTarget(self):
        self.GenerateList()
        self.colorMap[self.prevY][self.prevX] = orange
        self.prevX,self.prevY = random.choice(self.possibleSelect)
        self.colorMap[self.prevY][self.prevX] = green
        #print(self.colorMap)

    def GenerateList(self):
        for j in range(1,len(self.map)-1):
            for i in range(1,len(self.map[0])-1):
                if (self.map[j][i] == 1):
                    self.possibleSelect.append((i,j))

class Player:
    def __init__(self):
        self.posX = 150
        self.posY = 150
        self.angle = 0
        self.speed = 0.5
        self.cameraSens = 0.005
        self.points = 0

    def movement(self):
        keys = pygame.key.get_pressed()
        prevX = self.posX
        prevY = self.posY
        if (keys[pygame.K_s]):
            self.posX += -self.speed * math.cos(self.angle)
            self.posY += -self.speed * math.sin(self.angle)
        if (keys[pygame.K_w]):
            self.posX += self.speed * math.cos(self.angle) 
            self.posY += self.speed * math.sin(self.angle)
        if (keys[pygame.K_a]):
            self.posX += self.speed * math.sin(self.angle) 
            self.posY += -self.speed * math.cos(self.angle)
        if (keys[pygame.K_d]):
            self.posX += -self.speed * math.sin(self.angle) 
            self.posY += self.speed * math.cos(self.angle)

        if (map.map[int(self.posY // 100)] [int(self.posX // 100)] == 1):
            self.posX = prevX
            self.posY = prevY



        if (keys[pygame.K_LEFT]):
            self.angle -= self.cameraSens
        if (keys[pygame.K_RIGHT]):
            self.angle += self.cameraSens
        self.angle %= math.tau

        #print(player.posX,player.posY)

    def draw(self):
        pygame.draw.circle(screen,'green',(self.posX, self.posY),7)

    def shoot(self):
        GHPx, GHPy = Ray(self.angle).GetHitPoint()
        if (map.colorMap[int(GHPy // 100)][int(GHPx // 100)] == green): # if in colored block:
            player.points += 1 
            map.NewTarget()
            print("Your points:", player.points)

##########Class Objects##########
player = Player()
map = Map()
rays = [0] * numRays

############Functions############
"""
def DrawBullets():
    for i in range(len(bullets)):
        bullets[i].draw()
"""
map.NewTarget()


def TwoD():
    map.draw()
    player.draw()
    for i in range(numRays):
        rays[i].DrawRay()
    #rays[-1].DrawRay()

def ThreeD():
    map.newDraw()
    map.MiniMap()


######### Game Loop##############
while run:
    clock.tick(600)
    for i in range(numRays):
        '''
        if (i == 0):
            rays[i] = Ray(player.angle - player.cameraSens * 20)
        if i == 1:
            rays[i] = Ray(player.angle - player.cameraSens * 10)
        if i == 2:
            rays[i] = Ray(player.angle)
        if i == 3:
            rays[i] = Ray(player.angle + player.cameraSens * 10)
        if i == 4:
            rays[i] = Ray(player.angle + player.cameraSens * 20)
        '''

    ##################### FIX ##################### 
        if i == numRays / 2 - 0.5:
            rays[i] = Ray(player.angle)
        if i < numRays / 2:
            rays[i] = Ray(player.angle - FOV/numRays * (numRays/2 - i))
        if i > numRays / 2:
            rays[i] = Ray(player.angle + FOV/numRays * (i - numRays/2))

    pygame.display.set_caption(f'{clock.get_fps() : .1f}')
    for ev in pygame.event.get():
        if (ev.type == pygame.QUIT): #Quit
            run = False

        if (ev.type == pygame.MOUSEBUTTONDOWN): #Shoot
            player.shoot()

    #Game
    screen.fill((0,0,0))
    player.movement()

    #   SELECT    #

    #TwoD()
    ThreeD()


    '''
    DrawBullets()
    if (len(bullets) > 25): #Bullets Optimization
        bullets.pop(0)
    '''

    #Update
    pygame.display.update()
