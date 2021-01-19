import pygame
import random

#Close Santa's mouth when switch resets
#Speed up based on points
#Start/Stop Screen

#colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (55, 255, 15)
RED = (255, 0, 0)
BROWN = (216, 159, 80)
SKIN = (246, 186, 170)
GREY = (206, 206, 206)
BEARD = (173, 166, 164)
GOLD = (255, 229, 89)

points = 0
downa = False
downs = False
downd = False
downf = False


class Tile1:
    def __init__(self):
        self.w = 100
        self.l = random.randrange(120, 400)
        self.x = 50
        self.y = -500
        self.movey = 6
        self.colour = BROWN
        self.chocolist = []

        #To make the chocolate chips
        for i in range(8):
            chocox = random.randrange(5, 95)
            chocoy = random.randrange(10, (self.l - 10))
            self.chocolist.append([chocox, chocoy])#append to choco list


    def draw(self):
        pygame.draw.rect(screen, self.colour, (self.x, self.y, self.w, self.l))
        #Draws the chocolate chips
        for i in self.chocolist:
            pygame.draw.ellipse(screen, BLACK, [self.x + i[0], self.y + i[1], 10, 10])


    def move(self): 
        self.y += self.movey


class Tile2(Tile1):
    def __init__(self):
        super().__init__()
        self.x = 200
        self.movey = 5


class Tile3(Tile1):
    def __init__(self):
        super().__init__()
        self.x = 350
        self.movey = 6


class Tile4(Tile1):
    def __init__(self):
        super().__init__()
        self.x = 500
        self.movey = 7

class Santa1():
    def __init__(self, x, y, s):
        self.x = x
        self.y = y
        self.size = s
    def drawsanta(self, x):
        pygame.draw.polygon(screen, RED, [[(50 + self.x)/self.size, (10 + self.y)/self.size], [(-20 + self.x)/self.size, (100 + self.y)/self.size], [(120 + self.x)/self.size, (100 + self.y)/self.size]]) #Main hat shape
        pygame.draw.ellipse(screen, GREY, [(35 + self.x)/self.size, (-5 + self.y)/self.size, 30/self.size, 30/self.size]) #PomPom
        pygame.draw.rect(screen, SKIN, [(0 + self.x)/self.size, (100 + self.y)/self.size, 100/self.size, 100/self.size]) #Head
        pygame.draw.rect(screen, BLACK, [(20 + self.x)/self.size, (125 + self.y)/self.size, 10/self.size, 10/self.size]) #Eye Left
        pygame.draw.rect(screen, BLACK, [(70 + self.x)/self.size, (125 + self.y)/self.size, 10/self.size, 10/self.size]) #Eye Right
        pygame.draw.rect(screen, BEARD, [(-20 + self.x)/self.size, (100 + self.y)/self.size, 20/self.size, 70/self.size]) #Left Sideburn
        pygame.draw.rect(screen, BEARD, [(100 + self.x)/self.size, (100 + self.y)/self.size, 20/self.size, 70/self.size]) #Right Sideburn
        pygame.draw.polygon(screen, GREY, [[(-20 + self.x)/self.size, (170 + self.y)/self.size], [(50 + self.x)/self.size, (290 + self.y)/self.size], [(120 + self.x)/self.size, (170 + self.y)/self.size]]) #Beard
        pygame.draw.rect(screen, GREY, [(-30 + self.x)/self.size, (95 + self.y)/self.size, 160/self.size, 20/self.size]) #Hat Brim
        if x is True:
            pygame.draw.rect(screen, BLACK, [(45 + self.x) / self.size, (180 + self.y) / self.size, 20 / self.size, 20 / self.size])  # Mouth
        if x is False:
            pygame.draw.rect(screen, SKIN, [(45 + self.x)/self.size, (180 + self.y)/self.size, 20/self.size, 20/self.size]) #Mouth
    
        
def keyregistration(a, s, d, f, downa, downs, downd, downf, points, registrypoint):
    if a is True:
        try:
            if tile1.y <= registrypoint - tile1.l:
                points += 0
                downa = True

            elif (tile1.y >= registrypoint - tile1.l) and downa is False:
                points += 5

        except:
            pass
    if not a:
        downa = False

    # For the s key
    if s is True:
        try:
            if tile2.y <= registrypoint - tile2.l:
                points += 0
                downs = True

            elif (tile2.y >= registrypoint - tile2.l) and downs is False:
                points += 5

        except:
            pass
    if not s:
        downs = False

    #for the d key
    if d is True:
        try:
            if tile3.y <= registrypoint - tile3.l:
                points += 0
                downd = True

            elif (tile3.y >= registrypoint - tile3.l) and downd is False:
                points += 5

        except:
            pass
    if not d:
        downd = False

    # for the f key
    if f is True:
        try:
            if tile4.y <= registrypoint - tile4.l:
                points += 0
                downf = True

            elif (tile4.y >= registrypoint - tile4.l) and downf is False:
                points += 5

        except:
            pass
    if not f:
        downf = False

    return points, downa, downs, downd, downf

def deletetile(tile1, tile2, tile3, tile4, deletepoint):
    try:
        if tile1.y > deletepoint:
            del tile1
            tile1 = Tile1()
    except:
        pass

    try:
        if tile2.y > deletepoint:
            del tile2
            tile2 = Tile2()
    except:
        pass

    try:
        if tile3.y > deletepoint:
            del tile3
            tile3 = Tile3()
    except:
        pass

    try:
        if tile4.y > deletepoint:
            del tile4
            tile4 = Tile4()
    except:
        pass

    return tile1, tile2, tile3, tile4

def printscore(points):
    font = pygame.font.SysFont('Arial', 50, True, False)
    text = font.render(str(points), True, BLACK)
    screen.blit(text, [265, 0])

def drawcandycane(x):
    # Make bars like candy canes
    # Black bars to seperate the tiles
    pygame.draw.line(screen, RED, [x, 0], [x + 50, 100], 50)
    pygame.draw.line(screen, WHITE, [x, 100], [x + 50, 200], 50)
    pygame.draw.line(screen, RED, [x, 200], [x + 50, 300], 50)
    pygame.draw.line(screen, WHITE, [x, 300], [x + 50, 400], 50)
    pygame.draw.line(screen, RED, [x, 400], [x + 50, 500], 50)
    pygame.draw.line(screen, WHITE, [x, 500], [x + 50, 600], 50)
    pygame.draw.line(screen, RED, [x, 600], [x + 50, 700], 50)
    pygame.draw.line(screen, WHITE, [x, 700], [x + 50, 800], 50)

    #White Traingles
    pygame.draw.polygon(screen, WHITE, [[x - 25, 0], [x -25, 100], [x + 25, 100]])
    pygame.draw.polygon(screen, WHITE, [[x - 25, 200], [x - 25, 300], [x + 25, 300]])
    pygame.draw.polygon(screen, WHITE, [[x - 25, 400], [x - 25, 500], [x + 25, 500]])
    pygame.draw.polygon(screen, WHITE, [[x - 25, 600], [x - 25, 700], [x + 25, 700]])
    pygame.draw.polygon(screen, WHITE, [[x - 25, 800], [x - 25, 900], [x + 25, 900]])

    #Red Triangles
    pygame.draw.polygon(screen, RED, [[x - 25, 100], [x - 25, 200], [x + 25, 200]])
    pygame.draw.polygon(screen, RED, [[x - 25, 300], [x - 25, 400], [x + 25, 400]])
    pygame.draw.polygon(screen, RED, [[x - 25, 500], [x - 25, 600], [x + 25, 600]])
    pygame.draw.polygon(screen, RED, [[x - 25, 700], [x - 25, 800], [x + 25, 800]])
    pygame.draw.polygon(screen, RED, [[x - 25, 900], [x - 25, 1000], [x + 25, 1000]])

#Covers the excess from the candy canes
def drawwhiterect():
    pygame.draw.line(screen, GREEN, [100, 0], [100, 640], 100)
    pygame.draw.line(screen, GREEN, [250, 0], [250, 640], 100)
    pygame.draw.line(screen, GREEN, [400, 0], [400, 640], 100)
    pygame.draw.line(screen, GREEN, [550, 0], [550, 640], 100)

#Covers the cookie tiles when they move past the black line
def drawsantabackground():
    pygame.draw.rect(screen, GOLD, [50, 639, 100, 170])
    pygame.draw.rect(screen, GOLD, [200, 639, 100, 170])
    pygame.draw.rect(screen, GOLD, [350, 639, 100, 170])
    pygame.draw.rect(screen, GOLD, [500, 639, 100, 170])

def startscreen(done, space):
   while not done:
       for event in pygame.event.get():
           if event.type == pygame.QUIT:
               done = True

           if event.type == pygame.KEYDOWN:
               if event.key == pygame.K_SPACE:
                   done = True
                   space = True

           screen.fill(WHITE)

           font = pygame.font.SysFont('Arial', 50, True, False)
           text = font.render("Press SPACE to Start", True, BLACK)
           screen.blit(text, [150, 400])

           pygame.display.flip()
           # --- Limit to 60 frames per second

           clock.tick(60)

   return done, space


def restart(done, space):
   while not done:
       for event in pygame.event.get():
           if event.type == pygame.QUIT:
               done = True

           if event.type == pygame.KEYDOWN:
               if event.key == pygame.K_SPACE:
                   done = True
                   space = True

           screen.fill(WHITE)

           font = pygame.font.SysFont('Arial', 50, True, False)
           text = font.render("Press SPACE to Retry", True, BLACK)
           screen.blit(text, [150, 400])

           pygame.display.flip()
           # --- Limit to 60 frames per second
           clock.tick(60)
   return done, space

pygame.init()

#width and height of the screen
size = (650, 800)
screen = pygame.display.set_mode(size)

pygame.display.set_caption("My Game")

# Loop until the user clicks the close button.
done = False

# Used to manage how fast the screen updates
clock = pygame.time.Clock()

a = False
s = False
d = False
f = False

tile1 = Tile1()

tile2 = Tile2()

tile3 = Tile3()

tile4 = Tile4()

# -------- Main Program Loop -----------
while not done:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                a = True

            if event.key == pygame.K_s:
                s = True

            if event.key == pygame.K_d:
                d = True

            if event.key == pygame.K_f:
                f = True

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_a:
                a = False

            if event.key == pygame.K_s:
                s = False

            if event.key == pygame.K_d:
                d = False

            if event.key == pygame.K_f:
                f = False

    screen.fill(BLACK)

    #Draws the candy cane dividers
    drawcandycane(25)
    drawcandycane(175)
    drawcandycane(325)
    drawcandycane(475)
    drawcandycane(625)

    #To hide the edges of the candy canes
    drawwhiterect()

    #To delete the tiles after the move off the screen
    tile1, tile2, tile3, tile4 = deletetile(tile1, tile2, tile3, tile4, 640)

    #Draws and moves the tiles
    try:
        tile1.draw()
        tile1.move()

        tile2.draw()
        tile2.move()

        tile3.draw()
        tile3.move()

        tile4.draw()
        tile4.move()
    except:
        pass

    points, downa, downs, downd, downf, = keyregistration(a, s, d, f, downa, downs, downd, downf, points, 640)


    # Rectangles that hides the cookie tiles
    drawsantabackground()

    # When using the size manipulator note that the x and y coordiants
    # are also divided by the size multiplier
    santa1 = Santa1(150, 1300, 2)
    santa1.drawsanta(a)

    santa2 = Santa1(450, 1300, 2)
    santa2.drawsanta(s)

    santa2 = Santa1(750, 1300, 2)
    santa2.drawsanta(d)

    santa2 = Santa1(1050, 1300, 2)
    santa2.drawsanta(f)

    #Marker to indicate where the tile should be when you tap
    pygame.draw.line(screen, BLACK, [0, 640], [650, 640], 5)

    #Prints your current score
    printscore(points)


    pygame.display.flip()

    # --- Limit to 60 frames per second
    clock.tick(100)

# Close the window and quit.
pygame.quit()
