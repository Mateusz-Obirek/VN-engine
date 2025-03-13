from Window import Window
from Loader import Loader

class SceneManager:
    def __init__(self, game, activeScene = None, scenes = None):
        self.game = game
        self.activeScene = activeScene
        self.scenes = scenes
        Loader.loadScene(game, self.activeScene)
        
    def loadScenes(self, scenes):
        pass
    
    def setActiveScene(self, index):
        self.activeScene = self.scenes[index]
        Loader.loadScene(game, self.activeScene)