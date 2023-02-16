import pygame


class Alien(pygame.sprite.Sprite):
    def __init__(self, path, x_pos, y_pos, x_speed, y_speed):
        super().__init__()  # inherits all of sprite class's functionality
        self.image = pygame.image.load(path)  # creating a surface for the image
        self.rect = self.image.get_rect(center=(x_pos, y_pos))  # creating rectangle for the image
        self.x_speed = x_speed  # horizontal speed
        self.y_speed = y_speed  # vertical speed

    def update(self):
        self.rect.centerx += self.x_speed
        self.rect.centery += self.y_speed

        # will make sure that an alien that leaves the screen will be destroyed so that there aren't too many sprites
        # on screen
        if self.rect.centery >= 800:
            self.kill()
