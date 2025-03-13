import sys
sys.path.append('components')
from Window import Window 
from Loader import Loader
from Scene_manager import SceneManager
from Scene import Scene

game = Window()
#sceneManager = SceneManager(game, activeScene = Scene(backgroundColor='lightcoral'))

Loader.loadGame(game, './configs/preferences.txt')