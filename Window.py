import pyglet
from pyglet.window import key


class Window():
	def __init__(self):
		self.music = pyglet.resource.media('mp3sun.mp3')
		self.player = pyglet.media.Player()
		self.player.queue(self.music)
		self.player.play()
		self.playing = True
		self.window = pyglet.window.Window()
		self.event_loop = pyglet.app.EventLoop()

		# self.window.on_key_press = self.handleKey

	# @self.event_loop.event
	def on_window_close(window):
	    self.event_loop.exit()

	# @self.window.event
	def handleKey(symbol, modifiers):
	    print "You pressed " + str(symbol)
	    if symbol == key.Q:
	    	print 'yeah'
	    	self.window.close()
	    if symbol == key.S:
	    	self.player.pause()
	    	self.playing = False

window = Window()
pyglet.app.run()