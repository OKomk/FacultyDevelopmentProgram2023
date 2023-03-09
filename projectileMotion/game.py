import math
import pygame
import random
import time

# set up the screen
pygame.init()
pygame.mixer.init()
pygame.mixer.music.load('aww.mp3')
screen = pygame.display.set_mode((1600, 900))
clock = pygame.time.Clock()
pygame.display.set_caption("Basketball Game")

# set up colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

# set up fonts
font = pygame.font.SysFont(None, 30)

def calculate_trajectory(v, theta, x, y):
    # convert the angle to radians
    theta = math.radians(theta)
    # calculate the horizontal and vertical components of the velocity
    vx = v * math.cos(theta)
    vy = v * math.sin(-theta)

    # set up variables for the simulation
    t = 0.0
    dt = 0.05
    g = 9.8
    
    # simulate the motion of the ball
    i = 0
    xpos, ypos = [], []
    while y < 900:
        i+=1
        # calculate the new position of the ball
        x += vx * dt
        y += (vy * dt - 0.5 * g * dt ** 2)
        # print(x, y)
        # break
        
        # calculate the new velocity of the ball
        vy += g * dt
        xpos.append(x)
        ypos.append(y)
        # check if the ball has gone into the basket
        # if x > 700 and y < 100:
    return (xpos, ypos)

def getNewBasket():
    global basket_x, basket_y
    basket_x, basket_y = random.randint(400, 1100), random.randint(300, 700)

def getNewBall():
    global ball_x, ball_y
    ball_x, ball_y = random.randint(200, 400), random.randint(200, 500)

getNewBasket()
getNewBall()

isGoal = 0
score = 0
def main():
    global basket_x, basket_y, ball_x, ball_y
    global screen, isGoal, score
    bg_img = pygame.image.load('GraphCheck.jpg')
    bg_img = pygame.transform.scale(bg_img, (1600, 900))
    # set up variables for the game
    pygame.display.flip()
    theta = 55
    v = 75
    result = None
    # main game loop
    x, y = 0, 0

    while True:
        screen.blit(bg_img, (0, 0))
        # handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    quit()
                if event.key == pygame.K_UP:
                    theta += 1
                elif event.key == pygame.K_DOWN:
                    theta -= 1
                elif event.key == pygame.K_LEFT:
                    v -= 1
                elif event.key == pygame.K_RIGHT:
                    v += 1
                elif event.key == pygame.K_SPACE:
                    result = calculate_trajectory(v, theta, ball_x, ball_y)
                    x = y = 0
        
        # clear the screen
        # screen.fill(WHITE)
        
        # draw the basket
        pygame.draw.rect(screen, RED, [basket_x-25, basket_y-25, 50, 50])
        
        # draw the ball
        # ball_x = 200
        # ball_y = 200
        ball_radius = 10
        pygame.draw.circle(screen, BLACK, [ball_x, ball_y], ball_radius)
        
        # draw the text
        text1 = font.render("Angle: " + str(theta), True, BLACK)
        text2 = font.render("Velocity: " + str(v), True, BLACK)
        text3 = font.render("Score: " + str(score), True, BLACK)
        text4 = font.render("Press Space to Shoot", True, BLACK)
        text5 = font.render(f"({ball_x}, {ball_y})", True, BLACK)
        text6 = font.render(f"({basket_x}, {basket_y})", True, BLACK)


        
        screen.blit(text1, [10, 10])
        screen.blit(text2, [10, 40])
        screen.blit(text3, [10, 70])
        screen.blit(text4, [10, 100])
        screen.blit(text5, [ball_x, ball_y - 35])
        screen.blit(text6, [basket_x + 40, basket_y])
        if result is not None:
            if result:
                if (x<len(result[0])):
                    pygame.draw.circle(screen, BLACK, [result[0][x], result[1][y]], ball_radius)
                    if(math.pow(result[0][x]-basket_x, 2) + math.pow(result[1][y]-basket_y, 2) < 800):
                        text4 = font.render("GOAL!", True, BLACK)
                        screen.blit(text4, [350, 10])
                        pygame.display.update()
                        pygame.mixer.music.play()
                        time.sleep(2)
                        getNewBasket()
                        getNewBall()
                        isGoal = 1
                    else:
                        x += 1
                        y += 1
                else:
                    if not isGoal:
                        pass
                    
            # else:
            # result = None
        if(isGoal):
            isGoal = 0
            result = None
            score += 1

        clock.tick(200)
        # update the display
        pygame.display.update()
        # pygame.display.flip()

main()