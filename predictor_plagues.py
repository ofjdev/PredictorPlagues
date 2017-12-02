import pygame
import random
import copy

from Tkinter import Tk
from Tkinter import Button

blueP = (20, 34, 238)
greenP = (20, 240, 50)
green2 = (0, 128, 0)
green_chartreuse = (127, 255, 0)
redP = (230, 0, 20)
BLACK = (0, 0, 0)
GREY = (30, 30, 30)
sizeSquare = 40
WHITE = (255, 255, 255)

x = 0
y = 0
pygame.init()
quit = False

ciclos_plaga = 10

class cultiu():
    def __init__(self, x, y, n_x = 2, n_y = 2):
        self.x = x
        self.y = y
        self.n_x = n_x
        self.n_y = n_y

        self.contador_plaga = 0
        self.cultiu_plagat = False

        num_row_mod = y % 3
        if num_row_mod == 0:
            self.color_to_fill = greenP
        elif num_row_mod == 1:
            self.color_to_fill = green_chartreuse
        else:
            self.color_to_fill = green2

    def plagar(self):
        self.contador_plaga = 10
        self.cultiu_plagat = True
        self.color_to_fill = GREY

    def incr_ciclo_plaga_vecina(self, ciclos):
        self.contador_plaga += ciclos
        if self.contador_plaga == ciclos_plaga:
            self.plagar()

class mapa_camps():
    global pygame
    def __init__(self, camps, camps_x, camps_y, width_square = 40):
        
        self.files_canal_ppal = 2 # quants requadres ocupa el canal ppal
        self.files_desaigue_ppal = 0
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
        return ( ( camp.x * 2 + offset_x ) * self.width_square , ( ( camp.y + 1) * 2 + offset_y ) * self.width_square )

    def pinta_camp_color(self, camp, color):
        x,y = self.get_x_coord_camp(camp, 0, 0)
        self.pinta_quadrat_color(color, x, y)
        x,y = self.get_x_coord_camp(camp, 0, 1)
        self.pinta_quadrat_color(color, x, y)
        x,y = self.get_x_coord_camp(camp, 1, 0)
        self.pinta_quadrat_color(color, x, y)
        x,y = self.get_x_coord_camp(camp, 1, 1)
        self.pinta_quadrat_color(color, x, y)        

    #def pinta_camp_plagat(self, camp):
    #    self.pinta_camp_color(camp, GREY)

    def pinta_canals(self):
        for i in range(self.camps_x*2):
            self.pinta_quadrat_color(blueP, self.width_square * i, 0)
            self.screen.blit(pygame.font.Font(None, 32).render("==>", True, WHITE), [self.width_square * i, 0])
            self.pinta_quadrat_color(blueP, self.width_square * i, self.width_square)
            self.screen.blit(pygame.font.Font(None, 32).render("==>", True, WHITE), [self.width_square * i, self.width_square ])



# EXAMPLE TAKEN FROM:
# https://tpec05.blogspot.com.es/2016/02/programando-una-cuadricula-grid-en.html



mapa = {
    'camps': [],
    'rius': []
}

n_camps_x = 8
n_camps_y = 7

for i in range(0, n_camps_x):
    array = []
    mapa['camps'].append(array)
    for j in range(0, n_camps_y):
        nou_cultiu = cultiu(i, j)
        array.append(nou_cultiu)


def render_Map(camp):
    camp.screen.fill(BLACK)

    camp.pinta_camps_de_verd()

    #camp.pinta_camp_plagat(mapa['camps'][2][3])

    camp.pinta_canals()

    
    #clock.tick(5)

#while not quit:

#   for event in pygame.event.get():
#      if event.type == pygame.QUIT:
#         quit = True

map_camps = mapa_camps(mapa['camps'], n_camps_x, n_camps_y)
render_Map(map_camps)

window_control = Tk()
window_control.geometry("266x208")
window_control.title("Casos de prova")

def new_random(max):
    return int(random.random() * max)

def expandeix_plaga_1_cicle():
    # de moment s'expandeix per terra
    pass


plaga_iniciada = False

def event_inici_plaga():

    global map_camps
    global plaga_iniciada
    if not plaga_iniciada:
        x = new_random(n_camps_x)
        y = new_random(n_camps_y)

        cultiu = mapa['camps'][x][y]
        cultiu.plagar()

        render_Map(map_camps)

        pygame.display.flip()

    plaga_iniciada = True

b = Button(window_control, text="Inici Plaga", command=event_inici_plaga)
b.pack()

def event_incr_cicle():

    global map_camps
    #mapa_copy = copy.deepcopy(map_camps)

    for x in range(n_camps_x):
        for y in range(n_camps_y):
            cultiu = mapa['camps'][x][y]
            cultiu_plagat = cultiu.cultiu_plagat
            if cultiu_plagat:
                pass
                """for xx in range(3):
                    
                    for yy in range(3):
                        xx_1 = xx - 1
                        yy_1 = yy - 1
                        final_x = x + xx_1
                        final_y = y + yy_1
                        # center
                        # out of bounds
                        # 
                        if xx_1 + yy_1 > 0 \
                            and final_x >= 0 and final_y >= 0 and final_x < n_camps_x and final_y < n_camps_y and \
                            xx_1 * yy_1 == 0:
                            cultiu_vei = mapa_copy.camps[final_x][final_y]
                            cultiu_vei.plagar()"""
    
    render_Map(map_camps)

    #map_camps = mapa_copy

    pygame.display.flip()

    

b = Button(window_control, text="Passa un dia", command=event_incr_cicle)
b.pack()

window_control.mainloop()



#pygame.quit()