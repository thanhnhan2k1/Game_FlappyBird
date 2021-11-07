import pygame
import flappybird as fb
class Bird():
    def __init__(self):
        self.width = fb.BIRDWIDTH
        self.height = fb.BIRDHEIGHT
        self.x = (fb.WINDOWNWIDTH - self.width)/2
        self.y = (fb.WINDOWNHEIGHT - self.height)/2
        self.speed = 0 #toc do bay
        self.surface1 = fb.BIRDDOWN
        self.surface2 = fb.BIRDUP
        self.b_list = [fb.BIRDDOWN, fb.BIRDUP]
        self.bird_index = 0
        self.birdflap = pygame.USEREVENT+1
        pygame.time.set_timer(self.birdflap,150)

    def draw(self):
        if self.bird_index==0:
             fb.DISPLAYSURF.blit(self.surface1, (int(self.x), int(self.y)))
        else:
            fb.DISPLAYSURF.blit(self.surface2, (int(self.x), int(self.y)))
    #def rotate_bird(bird1):
        #new_bird = pygame.transform.rotozoom(bird1,-bird_movement*3,1)
        #return new_bird
    '''def bird_animation(self):
        new_bird=b_list[fb.bird_index]
        new_bird_rect= new_bird.get_rect(center=(100,bird_rect.centery))
        return new_bird,new_bird_rect'''
    def update(self, mouseClick):
        self.y += self.speed + 0.5*fb.G #y= vot + 1/2*g*t^2
        self.speed += fb.G #v=vo + g*t
        if mouseClick == True:
            self.speed = fb.SPEEDLY