from pygame import image

BLACK = (  0,   0,   0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
TRAILRED = (191, 19, 19)
INVISIBLEREDTRAIL = (100, 19, 19)
BOOSTREDTRAIL = (255, 209, 209)
TRAILBLUE = (117, 164, 255)

BACKGROUND = (10, 10, 10)
GRIDCOLOR = (0, 25, 0)

trailSize = 3
playerWidth = 11
GRIDLINES = 10


PLAYERLIVES = 3
SPEEDBOOSTFACTOR = 3
POWERUPTIME = 4
FPS = 60

# --- IMAGES --- #

ONE = image.load("../resources/1.png")
TWO = image.load("../resources/2.png")
THREE = image.load("../resources/3.png")
EXPLOSION = image.load("../resources/explosion.png")

IMAGES = [ONE, TWO, THREE]
for img in IMAGES:
    img.set_colorkey(BLACK)

# --- FUNCTIONS --- #

def sign(x):
    if (x == 0):
        return 0
    elif (x < 0):
        return -1
    else:
        return 1

def hasValue(x):
    if (x == 0):
        return 0
    else:
        return 1

def ceil(x):
    tmp = int(x)

    if (x == tmp):
        return x
    return tmp + 1

# --- GETTERS --- #

def getTrailColor(color, powerup):
    if (color == "RED"):
        if (powerup == True):
            return RED
        else:
            return RED

def getPowerup(color):
    if (color == "RED"):
        return "BOOST"

def getImages(color):
    if (color == "RED"):
        return ["../resources/RedCarU.png", "../resources/RedCarR.png", "../resources/RedCarD.png", "../resources/RedCarL.png"]
    if (color == "BLUE"):
        return ["../resources/BlueCarU.png", "../resources/BlueCarR.png", "../resources/BlueCarD.png",
                "../resources/BlueCarL.png"]

def isTrue(bool):
    if bool:
        return 1
    else:
        return 0



