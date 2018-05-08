#CK

from resources import colours

# | Page()
# |------------------------------------------
# | Parent class for each page of the game
# |------------------------------------
class Page():
    def __init__(self, surface):
        self.surface = surface

        self.objects = []

    # | draw()
    # |--------------------------------------------
    # | Clears the screen, and draws all objects
    # |---------------------------------------
    def draw(self):
        self.surface.fill(colours.black)
        self.drawObjects()

    # | drawObjects()
    # |--------------------------------------------
    # | Draws each item in the page's object list
    # |----------------------------------------
    def drawObjects(self):
        for object in self.objects:
            object.draw(self.surface)

    # | update()
    # |------------------------------------------------------
    # | Exists to be overridden. Not all pages will need to
    # | execute code each loop, so this acts as a place
    # | holder for the ones that don't; it allows
    # | main.py to call page.update() without
    # | an error if the page doesn't
    # | have and update() method
    # |--------------------
    def update(self):
        pass

    # | handleEvent()
    # |----------------------------------------------
    # | Allows the page to handle pygame generated
    # | events. Takes an event as a parameter
    # |----------------------------------
    def handleEvent(self, event):
        action = None

        return action

    # | addToObjects()
    # |------------------------------------------
    # | Adds items to the page's objects list
    # |----------------------------------
    def addToObjects(self, objects):
        if type(objects) != list:
           self.objects.append(objects)
        else:
            for object in objects:
                self.objects.append(object)



