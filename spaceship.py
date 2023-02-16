import pygame

screen = pygame.display.set_mode((1280, 720))  # create display surface


class Spaceship(pygame.sprite.Sprite):  # inherits from pygame.sprite.Sprite
    # path - file path of the image
    # x & y pos - position it will appear on screen
    def __init__(self, path, x_pos, y_pos):
        super().__init__()  # inherits all of sprite class's functionality
        self.neutral = pygame.image.load(path)  # neutral sprite for ship
        self.damaged = pygame.image.load("Space-battle Assets/damaged-ship.png")  # damaged ship sprite


        self.image = self.neutral  # creating a surface for the image
        self.rect = self.image.get_rect(center=(x_pos, y_pos))  # creating rectangle for the image
        self.health_surface = pygame.image.load("Space-battle Assets/shield.png")  # health
        self.health = 5

    """
    every sprite in pygame has an update method but we have to add our own functionality to it
    this update method can be called from the group & the group can call/exxecute the update method on 
    every sprite that has an update method simultaneously
    """

    def update(self):
        self.rect.center = pygame.mouse.get_pos()  # getting mouse position to move spaceship
        self.screen_constraint()
        self.display_health()

    # constraining the spaceship so it doesn't go out of bounds
    def screen_constraint(self):

        # fixing the right side
        if self.rect.right >= 1280:
            self.rect.right = 1280

        # fixing left side
        if self.rect.left <= 0:
            self.rect.left = 0

        # fixing top
        if self.rect.top <= 0:
            self.rect.top = 0

        # fixing bottom
        if self.rect.bottom >= 720:
            self.rect.bottom = 720

    def display_health(self):
        for index, icon in enumerate(range(self.health)):
            # each icon is set off by 10 pixels from the top
            # multiply each index by 40 to get their position on the x axis
            # starting at 10 to create more space from the left
            screen.blit(self.health_surface, (10 + index * 40, 10))

    def get_damage(self, damage_amount):
        damage_timer = 0
        self.health -= damage_amount
        self.image = self.damaged  # show damaged sprite

    def neutral_ship(self):
        self.image = self.neutral  # return to neutral state
