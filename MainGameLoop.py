from Loot_2D import *
from GameClasses import *
from functions import *

pygame.init()

# Init Program
#TILESIZE = 32
#ROOMWIDTH = 15
#ROOMHEIGHT = 15

# clock cycle
mainClock = pygame.time.Clock()

WORLD = WindowSurface(4*32, ROOMWIDTH, ROOMHEIGHT, "desert_world2")
ROOM = RoomSurface(ROOMWIDTH, ROOMHEIGHT, WORLD.playerSpawn)
PLAYER = Player(WORLD, 'link', 100, 100, 100, DOWN)
HUD = HUD()
COIN = Coin1()

WORLD.loadMap(ROOM)

# Game loop
while True:
    # draw current room to screen
    WORLD.drawMap(TILESIZE, ROOM.width, ROOM.height)

    COIN.getCoin(WORLD)
    COIN.drawCoin( WORLD)
    COIN.removeCoin(PLAYER.x + PLAYER.width/2, PLAYER.y + PLAYER.height/2)

    for event in pygame.event.get():  # event handling loop

        # handle exit button press
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                pygame.quit()
                sys.exit()

            PLAYER.handleKeyDown(event)

        elif event.type == KEYUP:
            PLAYER.handleKeyUp(event)

    if PLAYER.moveUp or PLAYER.moveDown or PLAYER.moveLeft or PLAYER.moveRight:
        # if in motion, then draw animation
        PLAYER.walkRunMotion(WORLD)

        curRate = 0

        if PLAYER.running:
            curRate = PLAYER.runRate
        else:
            curRate = PLAYER.walkRate

        if PLAYER.moveUp:
            PLAYER.move_Up(curRate, TILESIZE, WORLD, ROOM)
        if PLAYER.moveDown:
            PLAYER.move_Down(curRate, TILESIZE, WORLD, ROOM)
        if PLAYER.moveLeft:
            PLAYER.move_Left(curRate, TILESIZE, WORLD, ROOM)
        if PLAYER.moveRight:
            PLAYER.move_Right(curRate, TILESIZE, WORLD, ROOM)

    else:
        PLAYER.idle(WORLD)

    # make sure the player does move off the screen
    PLAYER.boundsCheck(WORLD, ROOM)

    # check if the player has stepped into a portal object
    checkPortal(PLAYER, ROOM, WORLD)

    #       coinx, coiny, coinq = getCoin()
    #        world.loadMap()

    # TODO : add gui
    HUD.drawRect(WORLD.surface)
    # create menu gui - player menu / controls
    # windowSurface.blit(instructionSurf, instructionRect)

    pygame.display.update()
    mainClock.tick(30)  # fps / clock speed
