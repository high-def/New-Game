import pygame

class Cat(pygame.sprite.Sprite):
  def __init__(self, pos):
    super().__init__()
    self.image = pygame.image.load("cat.png")
    self.image = pygame.transform.smoothscale(self.image,(40,40))
    self.rect = self.image.get_rect()     
    self.rect.center = pos 
    self.image = pygame.transform.rotate(self.image, -90)
    self.speed = pygame.math.Vector2(0, 0)

  def update(self):
    self.rect.move_ip(self.speed)

  def reset(self, pos):
    self.rect.center = pos
  
  def check_reset(self, end_pos):
    return self.rect.center[0] > end_pos