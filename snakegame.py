import pygame
import time

class YilanOyunu:
    def __init__(self):
        self.yilan_x = 10
        self.yilan_y = 10
        self.yem_x = 20
        self.yem_y = 20
        self.oyun_alani_genislik = 500
        self.oyun_alani_yukseklik = 500
        self.ekran = pygame.display.set_mode((self.oyun_alani_genislik, self.oyun_alani_yukseklik))
        self.oyun_bitti = False
        self.clock = pygame.time.Clock()

    def oyunu_baslat(self):
        pygame.init()

        while not self.oyun_bitti:
            for event in pygame.event.get():
                if event.type == pygame. QUIT:
                    self.oyun_bitti = True

            self.ekran.fill((0, 0, 0))
            pygame.draw.rect(self.ekran, (255, 0, 0), (self.yem_x, self.yem_y, 10, 10))  #yiyecek
            pygame.draw.rect(self.ekran, (0, 255, 0), (self.yilan_x, self.yilan_y, 10, 10)) #yılan

            pygame.display.update()
            self.clock.tick(10)

        pygame.quit()

oyun = YilanOyunu()
oyun.oyunu_baslat()