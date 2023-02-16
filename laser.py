import pygame


class Laser(pygame.sprite.Sprite):
    def __init__(self, path, pos, speed):
        super().__init__()  # inherits all of sprite class's functionality
        self.image = pygame.image.load(path)  # creating a surface for the image
        self.rect = self.image.get_rect(center=pos)  # creating rectangle for the image and position of the mouse
        self.speed = speed  # speed - the speed it will travel

    def update(self):
        # will move the center of the rectangle on y axis by speed
        # negative so it goes upwards
        self.rect.centery -= self.speed

        # kill laser if it is off screen
        if self.rect.centery <= -100:
            self.kill()
