from random import randint
from sys import exit
from textwrap import dedent #Removes indented whitespace in """ strings

#Scene is-a object that requires a enter() function 
class Scene(object):
    def enter(self):
        print("This scene is not yet configured.")
        print("Subclass it and implement enter().")
        exit(1)


class Engine(object):
    def __init__(self, scene_map):  #init needs self
        self.scene_map = scene_map

    def play(self):
        current_scene = self.scene_map.opening_scene()
        last_scene = self.scene_map.next_scene('finished')

        while current_scene != last_scene:
            next_scene_name = current_scene.enter()
            current_scene = self.scene_map.next_scene(next_scene_name)

        # be sure to print out the last scene
        current_scene.enter()


class Death(Scene):
    #Dictionary of quips
    quips = [
        "You dead 1",
        "You dead 2"
    ]

    def enter(self):
        print(Death.quips[randint(0, len(self.quips) - 1)])
        exit(1)


class one(Scene):
    def enter(self):
        print(dedent("""
			Type 3 to live or anything else to die
			"""))

        good_pod = 3

        guess = input("[number #]> ")

        if int(guess) != good_pod:
            print(dedent(f"""
                You are dying.
                """))

            return 'death'
        else:
            print(dedent(f"""
				You won!
				"""))

            return 'finished'


class Finished(Scene):
    def enter(self):
        print("You won! Good job.")
        return 'finished'


class Map(object):
    #Dictionary of scenes
    scenes = {
        'one': one(),
        'death': Death(),
        'finished': Finished()
    }

    def __init__(self, start_scene):    #init needs self
        self.start_scene = start_scene

    def next_scene(self, scene_name):   #init needs self
        val = Map.scenes.get(scene_name)
        return val

    def opening_scene(self):
        return self.next_scene(self.start_scene)


a_map = Map('one')
a_game = Engine(a_map)
a_game.play()