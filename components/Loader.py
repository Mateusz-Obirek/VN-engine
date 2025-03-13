from Window import Window 

class Loader:
    def loadGame(game, path):
        f = open(path, 'r')
        preferences = f.readlines()
        for i in range(len(preferences)):
            pref = preferences[i][:-1]
            preferences[i] = pref

        title, screenSize = preferences[::]
        
        game.setTitle(title)
        game.setDisplay(screenSize)
        game.start()
    def loadScene(game, scene):
        #backgroundColor, backgroundImage
        #actor1, actor2, actor3
        #print(scene.backgroundColor)
        #game.setBackgroundColor(scene.backgroundColor)
        pass
    