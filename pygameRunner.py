# a perspective running game
# collect powerups and avoid obstacles
import pygame
from random import randint

def rectCollision(rect1 : pygame.Rect, rect2 : pygame.Rect):
    collide = False
    if rect1.bottom > rect2.top:
        if rect1.top < rect2.bottom:
            if rect1.left < rect2.right:
                if rect1.right > rect2.left:
                    collide = True
    return collide

pygame.init() # initalise

width = 512
height = 720

screen = pygame.display.set_mode((width,height)) #creates a surface
clock = pygame.time.Clock()

# variable definition
trackSpaceW = width * 0.2
trackSpaceH = height * 0.3
trackW = width - trackSpaceW*2
trackH = height - trackSpaceH
trackPoly = [(0,height),(trackSpaceW,trackSpaceH),(width-trackSpaceW,trackSpaceH),(width,height)]

# Lanes
charW, charH = width*0.1, height*0.1
padding = 10
leftLaneBottom = width/6
leftLaneTop = trackSpaceW + trackW/6
middleLane = width/2
rightLaneBottom = width/6*5
rightLaneTop = trackSpaceW + trackW/6*5

obsW = width * 0.1
obsSpeed = 1
leftLaneRatio = (leftLaneBottom - leftLaneTop) / width
rightLaneRatio = (rightLaneBottom - rightLaneTop) / width

obs1yOfsett = randint(int(-height/3),0) #FIXED
obs1x = leftLaneTop - obsW/2 + leftLaneRatio * obs1yOfsett #FIXED
obs1y = trackSpaceH - obsW/2 + obs1yOfsett
obs1Counter = 0
obs1xVel = obsSpeed * leftLaneRatio
obs1yVel = obsSpeed

obs2yOfsett = randint(int(-height/3),0)
obs2x = middleLane - obsW/2
obs2y = trackSpaceH - obsW/2 + obs2yOfsett
obs2Counter = 0
obs2yVel = obsSpeed

obs3yOfsett = randint(int(-height/3),0) #FIXED
obs3x = rightLaneTop - obsW/2 + rightLaneRatio * obs3yOfsett #FIXED
obs3y = trackSpaceH - obsW/2 + obs3yOfsett
obs3Counter = 0
obs3xVel = obsSpeed * rightLaneRatio
obs3yVel = obsSpeed

# Player Variables
currentPlayerLane = "middle"
playerX = middleLane
dead = False

while True: # game loop
    # Process player inputs.
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            raise SystemExit
        # Moving character into left and right lanes
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a or event.key == pygame.K_LEFT:
                if currentPlayerLane == "middle":
                    playerX = leftLaneBottom
                    currentPlayerLane = "left"
                if currentPlayerLane == "right":
                    playerX = middleLane
                    currentPlayerLane = "middle"
            if event.key == pygame.K_d or event.key == pygame.K_RIGHT:
                if currentPlayerLane == "middle":
                    playerX = rightLaneBottom
                    currentPlayerLane = "right"
                if currentPlayerLane == "left":
                    playerX = middleLane
                    currentPlayerLane = "middle"

    if not dead:
        screen.fill((80,100,255))  # Fill the display with a solid color
        track = pygame.draw.polygon(screen,(255,0,0),trackPoly)

        # Obstacles
        obsW = width * 0.1
        obs1W = obsW * (obs1y/height * 2)
        obs2W = obsW * (obs2y/height * 2)
        obs3W = obsW * (obs3y/height * 2)

        obs1x += obs1xVel * ((abs(obs1y) + 1) * 0.02) #FIXED
        obs1y += obs1yVel * ((abs(obs1y) + 1) * 0.02)

        obs2x = middleLane - obs2W/2 #ADDED
        obs2y += obs2yVel * ((abs(obs2y) + 1) * 0.02)

        obs3x += obs3xVel * ((abs(obs3y) + 1) * 0.02) #FIXED
        obs3y += obs3yVel * ((abs(obs3y) + 1) * 0.02)

        obs1 = pygame.Rect(obs1x,obs1y,obs1W,obs1W)
        obs2 = pygame.Rect(obs2x,obs2y,obs2W,obs2W)
        obs3 = pygame.Rect(obs3x,obs3y,obs3W,obs3W)

        pygame.draw.rect(screen, (0,255,0), obs1)
        pygame.draw.rect(screen, (0,255,0), obs2)
        pygame.draw.rect(screen, (0,255,0), obs3)

        if obs1.top > height:
            obs1yOfsett = randint(-height/3, 0) #FIXED
            obs1Counter += 1
            obs1x = leftLaneTop - obsW/2 + leftLaneRatio * obs1yOfsett #FIXED
            obs1y = trackSpaceH - obsW/2 + obs1yOfsett

        if obs2.top > height:
            obs2Counter += 1
            obs2yOfsett = randint(-height/3, 0) #FIXED
            obs2y = trackSpaceH - obsW/2 + obs2yOfsett

        if obs3.top > height:
            obs3yOfsett = randint(-height/3, 0) #FIXED
            obs3Counter += 1
            obs3x = rightLaneTop - obsW/2 + rightLaneRatio * obs3yOfsett #FIXED
            obs3y = trackSpaceH - obsW/2 + obs3yOfsett

        # Character
        charRect = pygame.Rect(playerX - charW/2, height - charH - padding,charW,charH)
        character = pygame.draw.rect(screen, (0,0,0), charRect)

        # Collisions of player with obstacles
        if dead == False:
            dead = rectCollision(charRect, obs1)
        if dead == False:
            dead = rectCollision(charRect, obs2)
        if dead == False:
            dead = rectCollision(charRect, obs3)
    else:
        screen.fill((0,0,0))  # Fill the display with black
        #TODO: draw game over text

    pygame.display.flip()  # Refresh on-screen display
    clock.tick(60)         # wait until next frame (at 60 FPS)
