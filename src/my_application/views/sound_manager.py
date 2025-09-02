import pygame

class Sound_manager():
    def __init__(self):
        pygame.mixer.init()
        self.sounds = {}
        self.music_loaded = False

    def load_sound(self,name,filepath):
        self.sounds[name] = pygame.mixer.Sound(filepath)
    
    def play_sound(self,name):
        if name in self.sounds:
            self.sounds[name].play()

    def load_music(self,filepath):
        pygame.mixer.music.load(filepath)
        self.music_loaded = True

    def play_music(self,loops=-1):
        if self.music_loaded == True:
            pygame.mixer.music.play()