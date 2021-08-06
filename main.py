import tkinter as tk
from random import randint, choice
WIDTH = 500
HEIGHT = 800

class Figures():
	"""docstring for Figures"""
	def __init__(self, canvas):
		self.colors = ['green', 'pink', 'red', 'cyan', 'yellow']


class s_shape(Figures):
	def create_figure(self):
		start = randint(0, 8)
		self.canvas = canvas
		color = choice(self.colors)
		res = []
		res.append(self.canvas.create_rectangle(start*(WIDTH//10), 0, (start+1)*(WIDTH//10), WIDTH//10, fill=color))
		res.append(self.canvas.create_rectangle(start*(WIDTH//10), WIDTH//10, (start+1)*(WIDTH//10), 2*WIDTH//10, fill=color))
		res.append(self.canvas.create_rectangle((start+1)*(WIDTH//10), WIDTH//10, (start+2)*(WIDTH//10), 2*WIDTH//10, fill=color))
		res.append(self.canvas.create_rectangle((start+1)*(WIDTH//10), 2*WIDTH//10, (start+2)*(WIDTH//10), 3*WIDTH//10, fill=color))
		return res


class z_shape(Figures):
	def create_figure(self):
		start = randint(0, 8)
		self.canvas = canvas
		color = choice(self.colors)
		res = []
		res.append(self.canvas.create_rectangle((start+1)*(WIDTH//10), 0, (start+2)*(WIDTH//10), WIDTH//10, fill=color))
		res.append(self.canvas.create_rectangle(start*(WIDTH//10), WIDTH//10, (start+1)*(WIDTH//10), 2*WIDTH//10, fill=color))
		res.append(self.canvas.create_rectangle((start+1)*(WIDTH//10), WIDTH//10, (start+2)*(WIDTH//10), 2*WIDTH//10, fill=color))
		res.append(self.canvas.create_rectangle((start)*(WIDTH//10), 2*WIDTH//10, (start+1)*(WIDTH//10), 3*WIDTH//10, fill=color))
		return res


class t_shape(Figures):
	def create_figure(self):
		start = randint(1, 8)
		self.canvas = canvas
		color = choice(self.colors)
		res = []
		res.append(self.canvas.create_rectangle(start*(WIDTH//10), 0, (start+1)*(WIDTH//10), WIDTH//10, fill=color))
		res.append(self.canvas.create_rectangle((start-1)*(WIDTH//10), 0, (start)*(WIDTH//10), WIDTH//10, fill=color))
		res.append(self.canvas.create_rectangle((start+1)*(WIDTH//10), 0, (start+2)*(WIDTH//10), WIDTH//10, fill=color))
		res.append(self.canvas.create_rectangle(start*(WIDTH//10), WIDTH//10, (start+1)*(WIDTH//10), 2*WIDTH//10, fill=color))
		return res


class l_shape(Figures):
	def create_figure(self):
		start = randint(0, 8)
		self.canvas = canvas
		color = choice(self.colors)
		res = []
		res.append(self.canvas.create_rectangle(start*(WIDTH//10), 0, (start+1)*(WIDTH//10), WIDTH//10, fill=color))
		res.append(self.canvas.create_rectangle(start*(WIDTH//10), WIDTH//10, (start+1)*(WIDTH//10), 2*WIDTH//10, fill=color))
		res.append(self.canvas.create_rectangle(start*(WIDTH//10), 2*WIDTH//10, (start+1)*(WIDTH//10), 3*WIDTH//10, fill=color))
		res.append(self.canvas.create_rectangle((start+1)*(WIDTH//10), 2*WIDTH//10, (start+2)*(WIDTH//10), 3*WIDTH//10, fill=color))
		return res


class mirr_l_shape(Figures):
	def create_figure(self):
		start = randint(1, 9)
		self.canvas = canvas
		color = choice(self.colors)
		res = []
		res.append(self.canvas.create_rectangle(start*(WIDTH//10), 0, (start+1)*(WIDTH//10), WIDTH//10, fill=color))
		res.append(self.canvas.create_rectangle(start*(WIDTH//10), WIDTH//10, (start+1)*(WIDTH//10), 2*WIDTH//10, fill=color))
		res.append(self.canvas.create_rectangle(start*(WIDTH//10), 2*WIDTH//10, (start+1)*(WIDTH//10), 3*WIDTH//10, fill=color))
		res.append(self.canvas.create_rectangle((start-1)*(WIDTH//10), 2*WIDTH//10, (start)*(WIDTH//10), 3*WIDTH//10, fill=color))
		return res


class line_shape(Figures):
	def create_figure(self):
		start = randint(0, 9)
		self.canvas = canvas
		color = choice(self.colors)
		res = []
		res.append(self.canvas.create_rectangle(start*(WIDTH//10), 0, (start+1)*(WIDTH//10), WIDTH//10, fill=color))
		res.append(self.canvas.create_rectangle(start*(WIDTH//10), WIDTH//10, (start+1)*(WIDTH//10), 2*WIDTH//10, fill=color))
		res.append(self.canvas.create_rectangle(start*(WIDTH//10), 2*WIDTH//10, (start+1)*(WIDTH//10), 3*WIDTH//10, fill=color))
		res.append(self.canvas.create_rectangle(start*(WIDTH//10), 3*WIDTH//10, (start+1)*(WIDTH//10), 4*WIDTH//10, fill=color))
		return res


class sqr_shape(Figures):
	def create_figure(self):
		start = randint(0, 8)
		self.canvas = canvas
		color = choice(self.colors)
		res = []
		res.append(self.canvas.create_rectangle(start*(WIDTH//10), 0, (start+1)*(WIDTH//10), WIDTH//10, fill=color))
		res.append(self.canvas.create_rectangle(start*(WIDTH//10), WIDTH//10, (start+1)*(WIDTH//10), 2*WIDTH//10, fill=color))
		res.append(self.canvas.create_rectangle((start+1)*(WIDTH//10), 0, (start+2)*(WIDTH//10), WIDTH//10, fill=color))
		res.append(self.canvas.create_rectangle((start+1)*(WIDTH//10), WIDTH//10, (start+2)*(WIDTH//10), 2*WIDTH//10, fill=color))
		return res


def draw_grid(canvas):
	lines_vertical = []
	lines_horisontal = []
	for i in range(0, 10):
		lines_vertical.append(canvas.create_line(WIDTH//10*i, 0, WIDTH//10*i, HEIGHT))
	for i in range(0, HEIGHT//(WIDTH//10)):
		lines_horisontal.append(canvas.create_line(0, i*(WIDTH//10), WIDTH, i*(WIDTH//10)))

	return lines_vertical, lines_horisontal


if __name__ == "__main__":
	root = tk.Tk()
	root.title("Tetris")
	root.configure(bg='#fff')

	canvas = tk.Canvas(root, bg='#fff', width=WIDTH, height=HEIGHT)
	canvas.pack()

	lines_vertical, lines_horisontal = draw_grid(canvas)
	all_objects = []
	all_figures = {
		's' : s_shape(canvas),
		'z' : z_shape(canvas),
		't' : t_shape(canvas),
		'l' : l_shape(canvas),
		'mirr_l' : mirr_l_shape(canvas),
		'line' : line_shape(canvas),
		'sqr' : sqr_shape(canvas)
	}

	keys = ['s', 'z', 't', 'l', 'mirr_l', 'line', 'sqr']

	all_objects.extend(all_figures.get(choice(keys)).create_figure())

	root.mainloop()
