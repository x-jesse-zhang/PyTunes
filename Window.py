import pyglet
from pyglet.window import key

class Window(pyglet.window.Window):
	def __init__(self):
		self.music = pyglet.resource.media('mp3sun.mp3')
		self.player = pyglet.media.Player()
		self.player.queue(self.music)
		self.player.play()

		self.playing = True
		
		self.window = pyglet.window.Window()
		pyglet.clock.schedule_interval(self.handle, 1/30.0)
		self.key_handler = key.KeyStateHandler()
		self.window.push_handlers(self.key_handler)

	# This merely proves a point and will be reimplemented in the GUI
	# TODO
	def handle(self, symbol):
	    if self.key_handler[key.D]:
	    	self.player.play()
	    	print "play"
	    if self.key_handler[key.S]:
	    	self.player.pause()
	    	print "pause"

window = Window()
pyglet.app.run()