import pygame
from Cat import *
from Ballofyarn import *

pygame.init()

screen_info = pygame.display.Info()
size = (width, height) = (screen_info.current_w, screen_info.current_h)

color = (50, 0, 100)
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()

def main():
  
  while True:
    clock.tick(60)
    screen.fill(color)
    pygame.display.flip()
    screen.blit(self.image, self.rect)




if __name__ == "__main__":
  main()
  