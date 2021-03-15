import sys, pygame

pygame.init()
pygame.font.init()

size = width, height = 1000, 800
screen = pygame.display.set_mode(size)

paddle1 = height / 2 - 75
paddle2 = height / 2 - 75
ballx = width / 2
bally = height / 2
ballySpeed = 0
ballxSpeed = -7

myfont = pygame.font.SysFont('Comic Sans MS', 30)

lost = False

pygame.display.update()
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP]:
        if paddle2 > 10.0:
            paddle2 -= 7
    if keys[pygame.K_DOWN]:
        if paddle2 < height - 10 - 150:
            paddle2 += 7

    if keys[pygame.K_w]:
        if paddle1 > 10.0:
            paddle1 -= 7
    if keys[pygame.K_s]:
        if paddle1 < height - 10 - 150:
            paddle1 += 7
    if lost:
        if keys[pygame.K_SPACE]:       
            paddle1 = height / 2 - 75
            paddle2 = height / 2 - 75
            ballx = width / 2
            bally = height / 2
            ballySpeed = 0
            ballxSpeed = -7
            lost = False
    
    bally += ballySpeed
    if bally >= height - 25:
        ballySpeed *= -1
    if bally <= 25:
        ballySpeed *= -1
    
    ballx += ballxSpeed
    if ballx < width / 2:
        if bally >= paddle1 and bally <= paddle1 + 150:
            if 40 + 25 - abs(ballxSpeed) <= ballx <= 40 + 25:
                ballxSpeed *= -1
                if ballySpeed == 0:
                    ballySpeed += 7
    if ballx > width / 2:
        if bally >= paddle2 and bally <= paddle2 + 150:
            if width - 40 - 25 + ballxSpeed >= ballx >= width - 40 - 25:
                ballxSpeed *= -1

    screen.fill((255, 255, 255))

    pygame.draw.rect(screen, (104, 198, 252), (30, paddle1, 10, 150))
    pygame.draw.rect(screen, (104, 198, 252), (width - 40, paddle2, 10, 150))
    pygame.draw.circle(screen, (255, 145, 0), (ballx, bally), 25)
    for dashLine in range(0, height, 40):
        pygame.draw.rect(screen, (0, 0, 0), (width / 2 - 5, dashLine, 10, 20))
    # if the ball is to far to the left then do something like say a discoraging and negative message 
    if ballx > width or ballx < 0:
        tExT = "You Lose. Hahaha you are bad at this. Press space to restart."
        lost = True
        textsurface = myfont.render(tExT, False, (112, 255, 119))
        textWidth, textHeight = myfont.size(tExT)

        screen.blit(textsurface, (width / 2 - textWidth / 2, height / 2 - textHeight / 2))
    pygame.display.flip()
    pygame.time.Clock().tick(60)
# Install git (git-scm.com)
# Add any features that you saw that you might like in your version
    # Score