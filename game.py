from sys import exit
from random import randint

class Scene(object):
    def enter(self):
        print "This scene is not yet configured. Subclass it and implement enter()."
        exit(1)

class Engine(object):

    def __init__(self, scene_map):
        self.scene_map = scene_map

    def play(self):
        current_scene = self.scene_map.opening_scene()
        last_scene = self.scene_map.next_scene('finished')

        while current_scene != last_scene:
				next_scene_name = current_scene.enter()
				current_scene = self.scene_map.next_scene(next_scene_name)

        current_scene.enter()	
		
class Finished(Scene):

    def enter(self):
        print "You won! Good job."
        return 'finished'
			
class Fail(Scene):
	
	def enter(self):
		print "Sorry you failed, please try again."
		exit(1)
		
class Start(Scene):
	
	def enter(self):
		print 'You are in an infinite loophole, you need to get out of there!'
		print 'There are two doors:'
		print '#1 Leads to heaven'
		print '#2 Leads to hell'
		print "But you don't know which door leads to what"
		print 'Which one will you choose?'
		b = raw_input('>' )
		n = randint(1,2)
		
		if b == str(n):
			return 'heaven'
		else:
			return 'hell'
			
class Heaven(Scene):

	def enter(self):
		print 'Congratulations, you have reached heaven!'
		print 'Do you regret your decision?'
		b = raw_input('>' )
		
		if b == 'yes' or b == 'y':
			return 'start'
		elif b == 'no' or b == 'n':
			print 'There are three doors in front of you:'
			print 'Entering door #1 makes you very wise.'
			print 'Entering door #2 gives you infinte money.'
			print 'Entering door #3 leads you to god.'
			print 'Which one do you choose?'
		
			a = raw_input("[keypad]>" )
		
			if a == '1':
				print 'You are selfless!!'
				return 'finished'
			elif a == '2':
				print 'You greedy bastard!, you stay in loophole for years and never come out.'
				return 'fail'
			elif a == '3':
				print 'You reach heaven and you die!'
				return 'fail'
			else:
				return 'heaven'
		
		else:
			print 'Please write correctly'
			return 'heaven'
					
class Hell(Scene):

	def enter(self):
		print 'BEWARE! YOU HAVE REACHED HELL'
		print 'You can still go back, going to hell is going to be a very difficult task'
		print 'Do you want to go back?'
		
		b = raw_input('>' )
		
		if b == 'yes' or  b =='y':
			print 'You are such a coward, you stay in loophole for years and never come out.'
			return 'fail'
		elif b == 'no' or b == 'n':
			print 'You are a brave man, you sucessfully come out of loophole'
			#print 'Congratulations, you win!'
			return 'finished'
		else:
			print 'Please write correctly'
			return 'hell'
			
class Map(object):

    scenes = { 'start': Start(),
	'hell': Hell(),
	'heaven': Heaven(),
	'fail': Fail(),
	'finished' : Finished()
	}

    def __init__(self, start_scene):
        self.start_scene = start_scene

    def next_scene(self, scene_name):
        val = Map.scenes.get(scene_name)
        return val

    def opening_scene(self):
        return self.next_scene(self.start_scene)


a_map = Map('start')
a_game = Engine(a_map)
a_game.play()