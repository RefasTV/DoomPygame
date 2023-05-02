#######Imports###############
import pygame, math

#### COLORS ####
orange = (255,171,0)
blue = (0,255,255)
green = (0,255,128)
white = (255,255,255)

########Variables############
H = 1000 #Ширина
W = 800 #Высота
run = True
#bullets = []
clock = pygame.time.Clock()
numRays = 101
screen = pygame.display.set_mode((H,W))
tile = 400
scaleX = H // numRays
dist = numRays / (2 * math.tan(math.pi/3))
FOV = math.pi / 3
deltaAngle = FOV / numRays        # FOV / numRays
pudge = pygame.image.load('pudge.png').convert_alpha() #download enemy pudge


###########Classes###########
class Enemy:
    def __init__(self):
        self.posX = 650
        self.posY = 750
        self.sprite = pudge
        self.size = 50 # cube 50 x 50
        self.baitDistance = 400
        self.moveSlow = 100
        #self.ray = Ray()

    def MoveToPlayer(self):
        if (abs(player.posX + player.posY - self.posX - self.posY) <= self.baitDistance):
            self.posX, self.posY = self.posX + (player.posX - self.posX) / self.moveSlow, self.posY + (player.posY - self.posY) / self.moveSlow
            print(self.posX, self.posY)



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
        return (200)
    
    def GetHitPoint(self):
        EnemysPos = []
        lenX = W * math.cos(self.angle) / 100 #Parts of rayX (1/100)
        lenY = W * math.sin(self.angle) / 100 #Parts of rayY (1/100)

        for i in range(1,100): # Founding the point by multiplying it on i
            if (map.map[int((player.posY + lenY * i) // 100)][int((player.posX + lenX * i) // 100)] == 1): # if in block
                return (player.posX + lenX * i, player.posY + lenY* i) # return points
            if ((int((player.posX + lenX * i) // 50),int((player.posY + lenY * i) // 50)) in EnemysPos): # if in enemy:
                EnemysPos.remove((int((player.posX + lenX * i) // 50),int((player.posY + lenY * i) // 50)))
                return (player.posX + lenX * i, player.posY + lenY* i) # return point
        return (0,0)
    
    def GetHitPointEnemy(self):
        EnemysPos = []
        lenX = W * math.cos(self.angle) / 100 #Parts of rayX (1/100)
        lenY = W * math.sin(self.angle) / 100 #Parts of rayY (1/100)
        for enem in enemyes:
            EnemysPos.append((int(enem.posX // 50), int(enem.posY // 50)))

        for i in range(1,100): # Founding the point by multiplying it on i
            if (map.map[int((player.posY + lenY * i) // 100)][int((player.posX + lenX * i) // 100)] == 1): # if in block
                return (0,0) # return points
            if ((int((player.posX + lenX * i) // 50),int((player.posY + lenY * i) // 50)) in EnemysPos): # if in enemy:
                EnemysPos.remove((int((player.posX + lenX * i) // 50),int((player.posY + lenY * i) // 50)))
                return (player.posX + lenX * i, player.posY + lenY* i) # return point

        return (0,0)


    def GetDistance(self):
        x,y = self.GetHitPoint()
        return (x - player.posX,y - player.posY)

'''
class Bullet:
    def __init__(self):
        self.angle = player.angle
        self.curX = player.posX
        self.curY = player.posY
    def nextPos(self):
        speed = 500
        return (player.posX + (player.posX + W * math.cos(player.angle)) / speed, player.posY + (player.posY + W * math.sin(player.angle)) / speed)

    def draw(self):
        if (W > self.curX > 0) and (H > self.curY > 0):
            pygame.draw.circle(screen,'white',self.nextPos(),3)
'''

class Map:
    def __init__(self):
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
            [1,'_','_','_',1,'_', '_',  '_','_',1],
            [1,'_', 1,  1, 1,  1,  1,   '_','_',1],
            [1,'_','_','_',1, '_', 1,   '_','_',1],
            [1,'_','_','_',1, '_', '_', '_','_',1],
            [1,'_', 1 ,'_','_','_', '_', 1,  1,1],
            [1,'_','_','_','_','_', '_', '_','_',1],
            [1, 1,  1,  1,  1,  1,  1,  1,  1,  1],
        ]

        self.colorMap = [
            [orange, orange,  orange,  orange,  orange,  orange,  orange,  orange, orange, orange],
            [orange, '_',   '_',      '_',     '_',     '_',     '_',      '_',     '_',    orange],
            [orange, '_',   '_',      '_',     '_',     '_',     '_',      '_',     '_',    orange],
            [orange, '_',   '_',      '_',     green,    green,    '_',    '_',     '_',    orange],
            [orange, '_',   '_',      '_',     green,    green,    '_',    '_',     '_',    orange],
            [orange, '_',   '_',      '_',     '_',     '_',     '_',     green,    '_',    orange],
            [orange, '_' ,  '_',      '_',     '_',     '_',     '_',     green,    '_',    orange],
            [orange, '_' ,  '_',      '_',     '_',     '_',     '_',     green,    '_',    orange],
            [orange, orange,orange,  orange,     '_',     '_',     '_',   green,  green,    orange],
            [orange, '_',   '_',      '_',     '_',     '_',     '_',     '_',     '_',    orange],
            [orange, '_',   '_',      '_',    orange,     '_',     '_',     '_',     '_',    orange],
            [orange, '_',   orange,   orange,   orange,   green,   green,     '_',     '_',    orange],
            [orange, '_',   '_',      '_',     orange,    '_',     green,     '_',     '_',    orange],
            [orange, '_',   '_',      '_',     orange,     '_',     '_',     '_',     '_',    orange],
            [orange, '_',  orange,  '_',     '_',     '_',     '_',     orange,     orange,    orange],
            [orange, '_',   '_',      '_',     '_',     '_',     '_',     '_',     '_',    orange],
            [orange, orange, orange,   orange,  orange,  orange,  orange,  orange,  orange,  orange],
        ]

    def draw(self): # Draw 2D
        for j in range(W // 100):
            for i in range(H // 100):
                if (self.map[j][i] == 1):
                    pygame.draw.rect(screen,'darkgray',(i*100, j*100, 100, 100))

    def drawWalls(self):
        for curRay in range(numRays):
            GHPx,GHPy = rays[curRay].GetHitPoint()
            proj_coff = dist * tile
            depth = rays[curRay].GetDepth() 
            proj_h = proj_coff / depth
            depth *= math.cos(player.angle - rays[curRay].angle) # Remove Fisheye


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

    def drawEnemyes(self):
        for curRay in range(numRays):
            GHPx,GHPy = rays[curRay].GetHitPointEnemy()
            if (GHPx,GHPy) != (0,0):
                screen.blit(pudge, (0,0))#screen,(scaleX * curRay, W / 2 - proj_h // 2, scaleX, proj_h))


    def newDraw(self): # Draw 3D
        self.drawWalls()
        self.drawEnemyes()
        
    def MiniMap(self):
        for j in range(len(map.map)):
            for i in range(len(map.map[0])):
                if (self.map[j][i] == 1):
                    pygame.draw.rect(screen,'darkgray',(i*10, j*10, 10, 10))
        pygame.draw.circle(screen,'green',(player.posX/10, player.posY/10),3)


class Player:
    def __init__(self):
        self.posX = 150
        self.posY = 150
        self.angle = 0
        self.speed = 0.5
        self.cameraSens = 0.005

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

    def draw(self):
        pygame.draw.circle(screen,'green',(self.posX, self.posY),7)

    
"""
    def Shoot(self):
        bullets.append(Bullet())
        print(bullets)
"""

############Functions############
"""
def DrawBullets():
    for i in range(len(bullets)):
        bullets[i].draw()
"""

def TwoD():
    map.draw()
    player.draw()
    for i in range(numRays):
        rays[i].DrawRay()
    #rays[-1].DrawRay()

def ThreeD():
    map.newDraw()
    map.MiniMap()


##########Class Objects##########
player = Player()
map = Map()
rays = [0] * numRays
enemyes = [Enemy()]

##########Run################
pygame.init()

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
        """
        if (ev.type == pygame.MOUSEBUTTONDOWN): #Shoot
            player.Shoot()
        """
    for i in range(len(enemyes)):
        enemyes[i].MoveToPlayer()
    #print(player.posX, player.posY)
    #Game
    screen.fill((0,0,0))
    player.movement()

    #   SELECT    #

    #TwoD()
    ThreeD()

    #screen.blit(pudge,(0,0))
    '''
    DrawBullets()
    if (len(bullets) > 25): #Bullets Optimization
        bullets.pop(0)
    '''

    #Update
    pygame.display.update()
