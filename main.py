import pygame, sys, random
from spaceship import Spaceship
from planet import Planet
from laser import Laser
from alien import Alien


# this function will contain the logic for the main game
def start_game():
    score = 0  # game score

    # laser
    laser_group.draw(screen)
    spaceship_group.draw(screen)  # bringing spaceship to the screen

    # bringing in planets
    planet_group.draw(screen)

    laser_group.update()  # updating laser
    spaceship_group.update()  # updating spaceship
    planet_group.update()  # updating planets

    # checking for collisions
    # checking for collision between ship and planet
    # if collision occurs, planet will be deleted
    if pygame.sprite.spritecollide(spaceship_group.sprite, planet_group, True):
        spaceship_group.sprite.get_damage(1)  # this will reduce the health and icons in game

    #  checking for collision between laser and planet
    #  using for loop to see if any laser in the group is intersecting with a planet in planet group
    for laser_sprite in laser_group:
        if pygame.sprite.spritecollide(laser, planet_group, True):
            score += 1  # if a planet is destroyed increase score by 1

    return score


# game over function
def game_over(score):
    # creating font object for game text
    game_font = pygame.font.Font("Space-battle Assets/LazenbyCompSmooth.ttf", 40)

    # this variable will store a surface which will have the entire text on it
    text_surface = game_font.render("GAME OVER ", True, (255, 255, 255))
    text_rect = text_surface.get_rect(center=(640, 360))

    score_font = pygame.font.Font("Space-battle Assets/LazenbyCompSmooth.ttf", 40)
    # this variable will store a surface which will have the score text on it
    score_surface = score_font.render(f"SCORE : {score}", True, (255, 255, 255))
    score_rect = score_surface.get_rect(center=(640, 400))

    screen.blit(text_surface, text_rect)
    screen.blit(score_surface, score_rect)


def win_message():
    # creating font object for game text
    game_font = pygame.font.Font("Space-battle Assets/LazenbyCompSmooth.ttf", 40)

    # this variable will store a surface which will have the entire text on it
    text_surface = game_font.render("Congratulations, You Have Committed Mass Genocide", True, (255, 255, 255))
    text_rect = text_surface.get_rect(center=(640, 360))

    text_surface2 = game_font.render("And Saved The Human Race! ", True, (255, 255, 255))
    text_surface2_rect = text_surface2.get_rect(center=(640, 400))

    screen.blit(text_surface, text_rect)
    screen.blit(text_surface2, text_surface2_rect)


pygame.init()  # initiate pygame
screen = pygame.display.set_mode((1280, 720))  # create display surface
clock = pygame.time.Clock()  # creating clock object
final_score = 0  # will display final score for the player

spaceship = Spaceship("Space-battle Assets/spaceship.png", 640, 500)
spaceship_group = pygame.sprite.GroupSingle()  # creating group single which will hold spaceship
spaceship_group.add(spaceship)  # adding spaceship tp group

# planets group
planet_group = pygame.sprite.Group()  # this group will contain many planets

# aliens group
alien_group = pygame.sprite.Group()

# creating a timer to spawn planets
PLANET_EVENT = pygame.USEREVENT + 0
pygame.time.set_timer(PLANET_EVENT, 250)  # timer will execute every 250 milliseconds

# creating timer for aliens
ALIEN_EVENT = pygame.USEREVENT + 1
pygame.time.set_timer(ALIEN_EVENT, 500)

# laser group
laser_group = pygame.sprite.Group()

# game loop
while True:
    for event in pygame.event.get():  # checking for player input
        if event.type == pygame.QUIT:
            pygame.quit()  # close the game
            sys.exit()

        # this block of code will create multiple planets which will come at the player
        if event.type == PLANET_EVENT:
            planet_path = random.choice(("Space-battle Assets/planet2.png", "Space-battle Assets/planet1.png"))
            random_x_pos = random.randrange(0, 1280)  # spawning a planet at a random x position
            random_y_pos = random.randrange(-500, -50)  # spawning a planet at a random y position
            random_x_speed = random.randrange(-1, 1)  # random horizontal speed
            random_y_speed = random.randrange(4, 10)  # ` random vertical speed
            planet = Planet(planet_path, random_x_pos, random_y_pos, random_x_speed, random_y_speed)
            planet_group.add(planet)

            alien_path = random.choice(
                ("Space-battle Assets/alien1.png", "Space-battle Assets/alien2.png", "Space-battle Assets/alien4.png"))
            alien = Alien(alien_path, random_x_pos, random_y_pos, random_x_speed, random_y_speed)

            # add aliens if you destroy more than 10 planets
            if final_score > 10:
                planet_group.add(alien)

        # this block of code will create a laser everytime the mouse button is clicked
        if event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()  # getting the position of the mouse
            laser = Laser("Space-battle Assets/Laser.png", pos, 20)  # creating laser
            laser_group.add(laser)  # adding new laser

        # when the game is over, click mouse to restart game
        if event.type == pygame.MOUSEBUTTONDOWN and spaceship_group.sprite.health <= 0:
            spaceship_group.sprite.health = 5  # reset health
            spaceship_group.sprite.neutral_ship()  # reset ship sprite
            planet_group.empty()  # empties all the planets to reset game
            final_score = 0  # resetting score

    screen.fill((0, 59, 89))  # setting the screen background colour to space blue

    # starting the game logic
    if spaceship_group.sprite.health > 0:
        final_score += start_game()  # adding up final score

    elif final_score >= 20:
        win_message()

    # game over condition
    elif spaceship_group.sprite.health <= 0:
        game_over(final_score)

    pygame.display.update()  # draw frame
    clock.tick(120)  # setting framerate
