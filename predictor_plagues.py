import pygame
import random


blueP = (20, 34, 238)
greenP = (20, 240, 50)
green2 = (0, 128, 0)
green_chartreuse = (127, 255, 0)
redP = (230, 0, 20)
BLACK = (0, 0, 0)
GREY = (30, 30, 30)
sizeSquare = 40

x = 0
y = 0
pygame.init()
quit = False

class cultiu():
    def __init__(self, x, y, n_x = 2, n_y = 2):
        self.x = x
        self.y = y
        self.n_x = n_x
        self.n_y = n_y

        num_row_mod = y % 3
        if num_row_mod == 0:
            self.color_to_fill = greenP
        elif num_row_mod == 1:
            self.color_to_fill = green_chartreuse
        else:
            self.color_to_fill = green2

class mapa_camps():
    global pygame
    def __init__(self, camps, camps_x, camps_y, width_square = 40):
        
        self.files_canal_ppal = 2 # quants requadres ocupa el canal ppal
        self.files_desaigue_ppal = 2
        self.camps_x = camps_x
        self.camps_y = camps_y
        self.camps = camps
        pygame.init()
        self.size_x = camps_x * 2 * width_square
        self.size_y = (camps_y * 2 + self.files_canal_ppal + self.files_desaigue_ppal) * width_square
        self.width_square = width_square
        self.eff_sq_wdth = self.width_square - 3
        self.screen = pygame.display.set_mode((self.size_x, self.size_y))
        pygame.display.set_caption("Predictor de Plagues: Cargol Poma")
        self.clock = pygame.time.Clock()


    def pinta_camps_de_verd(self):
        global pygame
        Ty = Tx = 0
        i = 1
        for i_camp in self.camps: #range(1, self.size_x, self.width_square):
            j = 1
            for j_camp in i_camp: #range(1, self.size_y, self.width_square):
                
                x, y = self.get_x_coord_camp(j_camp, 0, 0)
                self.pinta_camp_color(j_camp, j_camp.color_to_fill)
                #self.pinta_quadrat_color(color_to_fill, x, y)

                j += self.width_square
            i += self.width_square

    def pinta_quadrat_color(self, color, x, y):
        #print "x = "+str(x)
        #print "y = "+str(y)
        #print "eff_sq="+str(self.eff_sq_wdth)
        pygame.draw.rect(self.screen, color, [x, y, self.eff_sq_wdth, self.eff_sq_wdth], 0)

    def get_x_coord_camp(self, camp, offset_x, offset_y):
        return ( ( camp.x * 2 + offset_x ) * self.width_square +1 , ( ( camp.y + 1) * 2 + offset_y ) * self.width_square +1 )

    def pinta_camp_color(self, camp, color):
        x,y = self.get_x_coord_camp(camp, 0, 0)
        self.pinta_quadrat_color(color, x, y)
        x,y = self.get_x_coord_camp(camp, 0, 1)
        self.pinta_quadrat_color(color, x, y)
        x,y = self.get_x_coord_camp(camp, 1, 0)
        self.pinta_quadrat_color(color, x, y)
        x,y = self.get_x_coord_camp(camp, 1, 1)
        self.pinta_quadrat_color(color, x, y)        

    def pinta_camp_plagat(self, camp):
        self.pinta_camp_color(camp, GREY)

    def pinta_canals(self):
        for i in range(self.camps_x*2):
            self.pinta_quadrat_color(blueP, self.width_square * i, 0)
            self.pinta_quadrat_color(blueP, self.width_square * i, self.width_square)


# EXAMPLE TAKEN FROM:
# https://tpec05.blogspot.com.es/2016/02/programando-una-cuadricula-grid-en.html



mapa = {
    'camps': [],
    'rius': []
}

n_camps_x = 6
n_camps_y = 5

for i in range(0, n_camps_x):
    array = []
    mapa['camps'].append(array)
    for j in range(0, n_camps_y):
        nou_cultiu = cultiu(i, j)
        array.append(nou_cultiu)


class camp():
    def __init__(self):
        self.att = 0

def init_camps():
    pass



while not quit:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit = True

    camp = mapa_camps(mapa['camps'], n_camps_x, n_camps_y)

    camp.screen.fill(BLACK)

    camp.pinta_camps_de_verd()

    camp.pinta_camp_plagat(mapa['camps'][2][3])

    camp.pinta_canals()

    #camp.pinta_canals()

    colAl = (random.randrange(1, 255), random.randrange(1, 255), random.randrange(1, 255))
    #pygame.draw.rect(screen, colAl, [x, y, 38, 38], 0)
    pygame.display.flip()
    #clock.tick(5)
pygame.quit()